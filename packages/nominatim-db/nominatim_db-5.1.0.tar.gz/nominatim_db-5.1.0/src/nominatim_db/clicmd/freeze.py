# SPDX-License-Identifier: GPL-3.0-or-later
#
# This file is part of Nominatim. (https://nominatim.org)
#
# Copyright (C) 2024 by the Nominatim developer community.
# For a full list of authors see the git log.
"""
Implementation of the 'freeze' subcommand.
"""
import argparse

from ..db.connection import connect
from .args import NominatimArgs


class SetupFreeze:
    """\
    Make database read-only.

    About half of data in the Nominatim database is kept only to be able to
    keep the data up-to-date with new changes made in OpenStreetMap. This
    command drops all this data and only keeps the part needed for geocoding
    itself.

    This command has the same effect as the `--no-updates` option for imports.
    """

    def add_args(self, parser: argparse.ArgumentParser) -> None:
        pass  # No options

    def run(self, args: NominatimArgs) -> int:
        from ..tools import freeze

        with connect(args.config.get_libpq_dsn()) as conn:
            freeze.drop_update_tables(conn)
        freeze.drop_flatnode_file(args.config.get_path('FLATNODE_FILE'))

        return 0
