import logging

import click
from cloup import group, option

from .utils import formatter_settings


@group(invoke_without_command=True, formatter_settings=formatter_settings)
@option("--version", "show_version", is_flag=True, default=False)
def main(show_version: bool) -> None:
    logger = logging.getLogger("pypdf")
    logger.setLevel(logging.ERROR)
    if show_version:
        from .version import version  # noqa: PLC0415

        click.echo(version)


from . import commands  # noqa: E402 F401

if __name__ == "__main__":
    main(prog_name="pdf")
