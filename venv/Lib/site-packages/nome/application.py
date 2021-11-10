from cleo import Application
from cleo.config import ApplicationConfig

from . import __name__, __version__
from .npm_command import NpmCommand
from .pypi_command import PypiCommand

# Single command applications need a workaround:
# - https://github.com/sdispater/cleo/issues/71
# - https://github.com/sdispater/clikit/blob/0.6.2/src/clikit/config/default_application_config.py#L66
# - https://github.com/sdispater/clikit/blob/0.6.2/src/clikit/api/config/application_config.py
# - https://github.com/sdispater/clikit/blob/0.6.2/src/clikit/console_application.py
# - https://github.com/sdispater/cleo/issues/66
# - https://cleo.readthedocs.io/en/latest/single_command_tool.html
# The future version 1.0.0 seems to add native support for this:
# - https://github.com/sdispater/cleo/blob/1.0.0a4/cleo/application.py


# More info:
# - https://github.com/sdispater/clikit/blob/0.6.2/src/clikit/api/config/application_config.py#L257
# - https://github.com/sdispater/clikit/blob/0.6.2/src/clikit/api/config/application_config.py#L76
config = ApplicationConfig(name=__name__, version=__version__)
config.set_display_name(__name__)

# More info:
# - https://github.com/sdispater/cleo/blob/0.8.1/cleo/application.py
application = Application(config=config, complete=False)

application.add(NpmCommand())
application.add(PypiCommand())

# application.run()
