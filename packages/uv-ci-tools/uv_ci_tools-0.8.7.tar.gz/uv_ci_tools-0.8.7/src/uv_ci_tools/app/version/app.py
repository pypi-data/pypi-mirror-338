from uv_ci_tools.lib import cli

from . import bump

APP = cli.sub_app(__name__)


APP.command(bump.APP)
