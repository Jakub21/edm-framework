"""
[ EDM Framework ]
Jakub21, 2024/01
MIT License
--------------------------------
Used to dynamically import a Python module based on its filepath.
https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly
"""

from pathlib import Path
import importlib.util
import sys


def import_module(path: Path):
    """
    Dynamically import a Python module.
    path: Path to the file that's to be loaded.
    """
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[path.stem] = module
    spec.loader.exec_module(module)
    return module
