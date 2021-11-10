from http import HTTPStatus

import requests
from cleo import Command
from clikit.api.io import flags

from .constants import (
    AVAILABLE_MSG,
    HTTP_STATUS_CODE_MSG,
    NOT_AVAILABLE_MSG,
    NPM_BASE_URL,
)


class NpmCommand(Command):
    """
    Check the availability of a package name in npm

    npm
        {name : What package name do you want to see if it's available?}
    """

    def handle(self):
        name = self.argument("name")
        url = f"{NPM_BASE_URL}{name}"

        with requests.Session() as s:
            r = s.get(url)

            status_code = r.status_code
            updated_url = r.url

        status_code_description = HTTPStatus(status_code).phrase

        self.line(
            HTTP_STATUS_CODE_MSG.format(code=status_code, desc=status_code_description),
            verbosity=flags.VERBOSE,
        )

        is_available = status_code == 404

        if is_available:
            self.line(AVAILABLE_MSG.format(name=name))
        else:
            self.line(NOT_AVAILABLE_MSG.format(name=name, url=updated_url))
