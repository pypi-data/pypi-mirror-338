import pathlib
import typing

import tomlkit.items

from uv_ci_tools.lib import ver


def get_path():
    return pathlib.Path('pyproject.toml')


def update_pyproject_version(version_action: typing.Callable[[ver.Version], ver.Version]):
    pyproject_path = get_path()
    pyproject_document = tomlkit.parse(pyproject_path.read_text())
    project_item = pyproject_document['project']
    assert isinstance(project_item, tomlkit.items.Table)
    version_item = project_item['version']
    assert isinstance(version_item, tomlkit.items.String)
    old_version = ver.Version.load(version_item)
    new_version = version_action(old_version)
    project_item['version'] = new_version.dump()
    pyproject_path.write_text(pyproject_document.as_string())
    return new_version
