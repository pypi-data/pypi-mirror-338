import importlib
from pathlib import Path

import sys


def hot_reload_a_module_from_cwd(module_name) :
    """
    Import or reload a module from the current working directory where I run the scripts.

    Usage:
        mod = reload_import('some_package.some_module')
    """

    # Ensure the current working directory is in sys.path
    if not Path.cwd().as_posix() in sys.path :
        sys.path.insert(0 , Path.cwd().as_posix())

    # Import or reload (if already imported) the module
    if module_name in sys.modules :
        return importlib.reload(sys.modules[module_name])
    else :
        return importlib.import_module(module_name)
