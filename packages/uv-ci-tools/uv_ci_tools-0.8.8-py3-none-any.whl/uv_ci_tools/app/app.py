from uv_ci_tools.lib import cli

from . import version

APP = cli.main_app()

APP.command(version.APP)
