from __future__ import annotations

import sys

from devpkg import VersionChecker, VersionInfo, log_traceback

try:
    from enviromancer import Enviromancer
    from logician import Logician

    tools_available = True
except ImportError:
    tools_available = False


def dsbin_setup() -> VersionInfo:
    """Configure the system with standard setup options.

    Sets up exception handling and automatically records version information.

    Returns:
        VersionInfo object with version details. The return isn't needed if you aren't going to use
        it for anything, but it's available in case you need version information for something.
    """
    # Configure exception handling
    sys.excepthook = lambda exctype, value, tb: log_traceback((exctype, value, tb))

    # Automatically determine package name
    package_name = VersionChecker.get_caller_package_name()

    # Get and log version information
    version_info = VersionChecker.get_version_info(package_name)

    # Check if Enviromancer and Logician are available
    if tools_available:
        env = Enviromancer()
        env.add_bool("SHOW_VER")
        level = "DEBUG" if env.show_ver else "INFO"

        logger = Logician.get_logger(level=level, simple=True)
        logger.debug("Starting %s", version_info)

    return version_info
