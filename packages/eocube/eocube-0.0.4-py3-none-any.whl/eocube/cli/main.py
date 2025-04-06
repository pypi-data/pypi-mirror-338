# Copyright 2025 West University of Timisoara
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import importlib
import click

from eocube.utils.geospatialorg.cli import register as register_geospatialorg
from .auth import auth_cli


def is_installed(package_name):
    try:
        importlib.import_module(package_name)
        return True
    except ImportError:
        return False


@click.group()
def cli():
    pass


@cli.group()
def services():
    """Various Services"""
    pass


cli.add_command(services)
cli.add_command(auth_cli)

register_geospatialorg(services)

if __name__ == "__main__":
    cli()
