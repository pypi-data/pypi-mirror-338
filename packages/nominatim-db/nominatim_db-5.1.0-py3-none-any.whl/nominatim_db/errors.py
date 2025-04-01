# SPDX-License-Identifier: GPL-3.0-or-later
#
# This file is part of Nominatim. (https://nominatim.org)
#
# Copyright (C) 2024 by the Nominatim developer community.
# For a full list of authors see the git log.
"""
Custom exception and error classes for Nominatim.
"""


class UsageError(Exception):
    """ An error raised because of bad user input. This error will usually
        not cause a stack trace to be printed unless debugging is enabled.
    """
