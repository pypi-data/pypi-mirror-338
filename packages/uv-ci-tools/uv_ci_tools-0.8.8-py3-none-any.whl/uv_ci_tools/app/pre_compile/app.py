import subprocess

from uv_ci_tools.lib import ci, cli, util, uv

APP = cli.sub_app(__name__)


def get_installed_package(project_name: str):
    project_name_installed_package_map = {
        package.name: package for package in uv.list_installed_packages()
    }
    installed_package = project_name_installed_package_map.get(project_name)
    if installed_package is None:
        msg = f'Cannot find installed package for {project_name}'
        raise RuntimeError(msg)
    return installed_package


@APP.default
def pre_compile(*, ci_type: ci.Type = ci.Type.GITLAB, project_name: str | None = None):
    ci_ctx = ci_type.fill_context(ci.PartialContext(project_name=project_name))
    installed_package = get_installed_package(ci_ctx.project_name)
    with util.devnull() as devnull:
        subprocess.run(
            [installed_package.python_executable, '-m', 'compileall', installed_package.path],
            check=True,
            stdout=devnull,
        )
