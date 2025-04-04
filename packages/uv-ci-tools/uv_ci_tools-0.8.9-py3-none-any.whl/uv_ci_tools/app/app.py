from uv_ci_tools.lib import cli

from . import pre_compile, version

APP = cli.main_app()

APP.command(version.APP)
APP.command(pre_compile.APP)
