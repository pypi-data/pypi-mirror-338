#!/usr/bin/env python
#
# Copyright (c) 2020-2025 James Cherti
# URL: https://github.com/jamescherti/git-commitflow
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <https://www.gnu.org/licenses/>.
#
"""Git commit and push helper."""


import logging
import select
import subprocess
import sys
from termios import TCIFLUSH, tcflush

import colorama

from .git_commitflow import GitCommitFlow


def git_commitflow_cli():
    """The git-commitflow command-line interface."""
    logging.basicConfig(level=logging.INFO, stream=sys.stdout,
                        format="%(asctime)s %(name)s: %(message)s")
    colorama.init()

    # Check if there is any pending input in stdin without blocking
    # If input is available, flush the stdin buffer
    stdin, _, _ = select.select([sys.stdin], [], [], 0)
    if stdin and sys.stdin.isatty():
        tcflush(sys.stdin.fileno(), TCIFLUSH)

    try:
        GitCommitFlow().main()
    except subprocess.CalledProcessError as main_proc_err:
        print(f"Error: {main_proc_err}")
    except KeyboardInterrupt:
        print()
