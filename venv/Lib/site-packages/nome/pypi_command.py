from http import HTTPStatus

import requests
from cleo import Command
from clikit.api.io import flags

from .constants import (
    AVAILABLE_MSG,
    HTTP_STATUS_CODE_MSG,
    NOT_AVAILABLE_MSG,
    PYPI_BASE_URL,
)


class PypiCommand(Command):
    """
    Check the availability of a package name in PyPI

    pypi
        {name : What package name do you want to see if it's available?}
    """

    def handle(self):
        name = self.argument("name")
        url = f"{PYPI_BASE_URL}{name}"

        with requests.Session() as s:
            r = s.get(url)

            status_code = r.status_code
            updated_url = r.url

        # More info:
        # - https://stackoverflow.com/a/29880372
        # - https://github.com/python/cpython/blob/3.6/Lib/http/__init__.py
        # - https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
        status_code_description = HTTPStatus(status_code).phrase
        # or
        # status_code_description = HTTPStatus(status_code).description

        # Verbosity:
        # - https://github.com/sdispater/clikit/blob/0.6.2/src/clikit/api/io/flags.py
        # - https://github.com/sdispater/cleo/issues/49
        # - https://github.com/sdispater/cleo/blob/0.8.1/cleo/io/io_mixin.py
        # - https://github.com/sdispater/cleo/blob/0.8.1/cleo/commands/command.py#L224
        self.line(
            HTTP_STATUS_CODE_MSG.format(code=status_code, desc=status_code_description),
            verbosity=flags.VERBOSE,  # -v flag
        )

        is_available = status_code == 404  # Not Found

        if is_available:
            self.line(AVAILABLE_MSG.format(name=name))
        else:
            self.line(NOT_AVAILABLE_MSG.format(name=name, url=updated_url))
