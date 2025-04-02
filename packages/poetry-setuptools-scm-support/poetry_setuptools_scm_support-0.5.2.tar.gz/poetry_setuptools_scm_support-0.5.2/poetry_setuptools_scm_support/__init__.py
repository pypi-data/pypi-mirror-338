from cleo.commands.command import Command
from cleo.io.inputs.argument import Argument
from poetry.plugins.application_plugin import ApplicationPlugin
from poetry.factory import Factory

from setuptools_scm import Configuration, get_version
from setuptools_scm.version import calver_by_date, release_branch_semver_version

import warnings

def fxn():
    warnings.warn("deprecated", UserWarning)


class CalculateVersion(Command):
    """
    Calculates the version of the package.

    command:name {version-calculate : Controls output format}
    """

    name = "version-calculate"
    description = "Calculates the version of the package relying on setuptools_scm"

    args_description = """
        scm: formats according to setuptools_scm get_version default behavior. e.g. 0.1.dev1+g1e0ede4.
        date: formats current date and distance, e.g. 2025.4.1.1.dev1+g9d4edec . Scheme used is calver_by_date function
        branch: Use branch based versioning of library. Scheme used is release_branch_semver_version function
    """
    arguments = [
        Argument(name="format", description=args_description, default="scm", required=False),
    ]


    def __do_scm(self, c: Configuration) -> str:
        return get_version(root=c.root, relative_to=c.relative_to)

    def __do_date_and_dirty(self, c: Configuration) -> str:
        return get_version(root=c.root, relative_to=c.relative_to, version_scheme=calver_by_date)

    def __do_semver_branch(self, c: Configuration) -> str:
        return get_version(root=c.root, relative_to=c.relative_to, version_scheme=release_branch_semver_version)

    def handle(self) -> int:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            poetry = Factory().create_poetry()
            c = Configuration.from_file(str(poetry.file))

            format_to_use = self.argument("format")
            if format_to_use == "scm":
                v = self.__do_scm(c)
            elif format_to_use == "date":
                v = self.__do_date_and_dirty(c)
            elif format_to_use == "branch":
                v = self.__do_semver_branch(c)
            else:
                self.line_error(f"Unknown format: {format_to_use}")
                return 0

            confirm = self.ask(f'Dumping version "{v}" [Y/n]', 'Y')
            if confirm == "Y":
                poetry.pyproject.data.item('project').update(version=v)
                poetry.pyproject.file.write(poetry.pyproject.data)

            return 0


def factory():
    return CalculateVersion()

class ScmPlugin(ApplicationPlugin):
    @property
    def commands(self) -> list[type[Command]]:
        return [CalculateVersion]

    def activate(self, application):
        application.command_loader.register_factory("version-calculate", factory)
