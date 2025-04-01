# SPDX-License-Identifier: GPL-3.0-or-later
#
# This file is part of Nominatim. (https://nominatim.org)
#
# Copyright (C) 2025 by the Nominatim developer community.
# For a full list of authors see the git log.
"""
Nominatim configuration accessor.
"""
from typing import Union, Dict, Any, List, Mapping, Optional
import importlib.util
import logging
import os
import sys
from pathlib import Path
import json
import yaml

from dotenv import dotenv_values

from psycopg.conninfo import conninfo_to_dict

from .typing import StrPath
from .errors import UsageError
from . import paths

LOG = logging.getLogger()
CONFIG_CACHE: Dict[str, Any] = {}


def flatten_config_list(content: Any, section: str = '') -> List[Any]:
    """ Flatten YAML configuration lists that contain include sections
        which are lists themselves.
    """
    if not content:
        return []

    if not isinstance(content, list):
        raise UsageError(f"List expected in section '{section}'.")

    output = []
    for ele in content:
        if isinstance(ele, list):
            output.extend(flatten_config_list(ele, section))
        else:
            output.append(ele)

    return output


class Configuration:
    """ This class wraps access to the configuration settings
        for the Nominatim instance in use.

        All Nominatim configuration options are prefixed with 'NOMINATIM_' to
        avoid conflicts with other environment variables. All settings can
        be accessed as properties of the class under the same name as the
        setting but with the `NOMINATIM_` prefix removed. In addition, there
        are accessor functions that convert the setting values to types
        other than string.
    """

    def __init__(self, project_dir: Optional[Union[Path, str]],
                 environ: Optional[Mapping[str, str]] = None) -> None:
        self.environ = os.environ if environ is None else environ
        self.config_dir = paths.CONFIG_DIR
        self._config = dotenv_values(str(self.config_dir / 'env.defaults'))
        if project_dir is not None:
            self.project_dir: Optional[Path] = Path(project_dir).resolve()
            if (self.project_dir / '.env').is_file():
                self._config.update(dotenv_values(str(self.project_dir / '.env')))
        else:
            self.project_dir = None

        class _LibDirs:
            sql = paths.SQLLIB_DIR
            lua = paths.LUALIB_DIR
            data = paths.DATA_DIR

        self.lib_dir = _LibDirs()
        self._private_plugins: Dict[str, object] = {}

    def set_libdirs(self, **kwargs: StrPath) -> None:
        """ Set paths to library functions and data.
        """
        for key, value in kwargs.items():
            setattr(self.lib_dir, key, None if value is None else Path(value))

    def __getattr__(self, name: str) -> str:
        name = 'NOMINATIM_' + name

        if name in self.environ:
            return self.environ[name]

        return self._config[name] or ''

    def get_bool(self, name: str) -> bool:
        """ Return the given configuration parameter as a boolean.

            Parameters:
              name: Name of the configuration parameter with the NOMINATIM_
                prefix removed.

            Returns:
              `True` for values of '1', 'yes' and 'true', `False` otherwise.
        """
        return getattr(self, name).lower() in ('1', 'yes', 'true')

    def get_int(self, name: str) -> int:
        """ Return the given configuration parameter as an int.

            Parameters:
              name: Name of the configuration parameter with the NOMINATIM_
                prefix removed.

            Returns:
              The configuration value converted to int.

            Raises:
              ValueError: when the value is not a number.
        """
        try:
            return int(getattr(self, name))
        except ValueError as exp:
            LOG.fatal("Invalid setting NOMINATIM_%s. Needs to be a number.", name)
            raise UsageError("Configuration error.") from exp

    def get_str_list(self, name: str) -> Optional[List[str]]:
        """ Return the given configuration parameter as a list of strings.
            The values are assumed to be given as a comma-sparated list and
            will be stripped before returning them.

            Parameters:
              name: Name of the configuration parameter with the NOMINATIM_
                prefix removed.

            Returns:
              (List[str]): The comma-split parameter as a list. The
                elements are stripped of leading and final spaces before
                being returned.
              (None): The configuration parameter was unset or empty.
        """
        raw = getattr(self, name)

        return [v.strip() for v in raw.split(',')] if raw else None

    def get_path(self, name: str) -> Optional[Path]:
        """ Return the given configuration parameter as a Path.

            Parameters:
              name: Name of the configuration parameter with the NOMINATIM_
                prefix removed.

            Returns:
              (Path): A Path object of the parameter value.
                  If a relative path is configured, then the function converts this
                  into an absolute path with the project directory as root path.
              (None): The configuration parameter was unset or empty.
        """
        value = getattr(self, name)
        if not value:
            return None

        cfgpath = Path(value)

        if not cfgpath.is_absolute():
            assert self.project_dir is not None
            cfgpath = self.project_dir / cfgpath

        return cfgpath.resolve()

    def get_libpq_dsn(self) -> str:
        """ Get configured database DSN converted into the key/value format
            understood by libpq and psycopg.
        """
        dsn = self.DATABASE_DSN

        def quote_param(param: str) -> str:
            key, val = param.split('=')
            val = val.replace('\\', '\\\\').replace("'", "\\'")
            if ' ' in val:
                val = "'" + val + "'"
            return key + '=' + val

        if dsn.startswith('pgsql:'):
            # Old PHP DSN format. Convert before returning.
            return ' '.join([quote_param(p) for p in dsn[6:].split(';')])

        return dsn

    def get_database_params(self) -> Mapping[str, Union[str, int, None]]:
        """ Get the configured parameters for the database connection
            as a mapping.
        """
        dsn = self.DATABASE_DSN

        if dsn.startswith('pgsql:'):
            return dict((p.split('=', 1) for p in dsn[6:].split(';')))

        return conninfo_to_dict(dsn)

    def get_import_style_file(self) -> Path:
        """ Return the import style file as a path object. Translates the
            name of the standard styles automatically into a file in the
            config style.
        """
        style = getattr(self, 'IMPORT_STYLE')

        if style in ('admin', 'street', 'address', 'full', 'extratags'):
            return self.lib_dir.lua / f'import-{style}.lua'

        return self.find_config_file('', 'IMPORT_STYLE')

    def get_os_env(self) -> Dict[str, str]:
        """ Return a copy of the OS environment with the Nominatim configuration
            merged in.
        """
        env = {k: v for k, v in self._config.items() if v is not None}
        env.update(self.environ)

        return env

    def load_sub_configuration(self, filename: StrPath,
                               config: Optional[str] = None) -> Any:
        """ Load additional configuration from a file. `filename` is the name
            of the configuration file. The file is first searched in the
            project directory and then in the global settings directory.

            If `config` is set, then the name of the configuration file can
            be additionally given through a .env configuration option. When
            the option is set, then the file will be exclusively loaded as set:
            if the name is an absolute path, the file name is taken as is,
            if the name is relative, it is taken to be relative to the
            project directory.

            The format of the file is determined from the filename suffix.
            Currently only files with extension '.yaml' are supported.

            YAML files support a special '!include' construct. When the
            directive is given, the value is taken to be a filename, the file
            is loaded using this function and added at the position in the
            configuration tree.
        """
        configfile = self.find_config_file(filename, config)

        if str(configfile) in CONFIG_CACHE:
            return CONFIG_CACHE[str(configfile)]

        if configfile.suffix in ('.yaml', '.yml'):
            result = self._load_from_yaml(configfile)
        elif configfile.suffix == '.json':
            with configfile.open('r', encoding='utf-8') as cfg:
                result = json.load(cfg)
        else:
            raise UsageError(f"Config file '{configfile}' has unknown format.")

        CONFIG_CACHE[str(configfile)] = result
        return result

    def load_plugin_module(self, module_name: str, internal_path: str) -> Any:
        """ Load a Python module as a plugin.

            The module_name may have three variants:

            * A name without any '.' is assumed to be an internal module
              and will be searched relative to `internal_path`.
            * If the name ends in `.py`, module_name is assumed to be a
              file name relative to the project directory.
            * Any other name is assumed to be an absolute module name.

            In either of the variants the module name must start with a letter.
        """
        if not module_name or not module_name[0].isidentifier():
            raise UsageError(f'Invalid module name {module_name}')

        if '.' not in module_name:
            module_name = module_name.replace('-', '_')
            full_module = f'{internal_path}.{module_name}'
            return sys.modules.get(full_module) or importlib.import_module(full_module)

        if module_name.endswith('.py'):
            if self.project_dir is None or not (self.project_dir / module_name).exists():
                raise UsageError(f"Cannot find module '{module_name}' in project directory.")

            if module_name in self._private_plugins:
                return self._private_plugins[module_name]

            file_path = str(self.project_dir / module_name)
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            if spec:
                module = importlib.util.module_from_spec(spec)
                # Do not add to global modules because there is no standard
                # module name that Python can resolve.
                self._private_plugins[module_name] = module
                assert spec.loader is not None
                spec.loader.exec_module(module)

                return module

        return sys.modules.get(module_name) or importlib.import_module(module_name)

    def find_config_file(self, filename: StrPath,
                         config: Optional[str] = None) -> Path:
        """ Resolve the location of a configuration file given a filename and
            an optional configuration option with the file name.
            Raises a UsageError when the file cannot be found or is not
            a regular file.
        """
        if config is not None:
            cfg_value = getattr(self, config)
            if cfg_value:
                cfg_filename = Path(cfg_value)

                if cfg_filename.is_absolute():
                    cfg_filename = cfg_filename.resolve()

                    if not cfg_filename.is_file():
                        LOG.fatal("Cannot find config file '%s'.", cfg_filename)
                        raise UsageError("Config file not found.")

                    return cfg_filename

                filename = cfg_filename

        search_paths = [self.project_dir, self.config_dir]
        for path in search_paths:
            if path is not None and (path / filename).is_file():
                return path / filename

        LOG.fatal("Configuration file '%s' not found.\nDirectories searched: %s",
                  filename, search_paths)
        raise UsageError("Config file not found.")

    def _load_from_yaml(self, cfgfile: Path) -> Any:
        """ Load a YAML configuration file. This installs a special handler that
            allows to include other YAML files using the '!include' operator.
        """
        yaml.add_constructor('!include', self._yaml_include_representer,
                             Loader=yaml.SafeLoader)
        return yaml.safe_load(cfgfile.read_text(encoding='utf-8'))

    def _yaml_include_representer(self, loader: Any, node: yaml.Node) -> Any:
        """ Handler for the '!include' operator in YAML files.

            When the filename is relative, then the file is first searched in the
            project directory and then in the global settings directory.
        """
        fname = loader.construct_scalar(node)

        if Path(fname).is_absolute():
            configfile = Path(fname)
        else:
            configfile = self.find_config_file(loader.construct_scalar(node))

        if configfile.suffix != '.yaml':
            LOG.fatal("Format error while reading '%s': only YAML format supported.",
                      configfile)
            raise UsageError("Cannot handle config file format.")

        return yaml.safe_load(configfile.read_text(encoding='utf-8'))
