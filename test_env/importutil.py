from importlib import import_module as _import_module
from pathlib import Path
from sys import modules
from typing import Callable

Submit = Callable
Module = str


def import_module(path: Path) -> Module:
    """imports module by given path, keep it opened"""
    to_import = path.stem
    _import_module(to_import)
    return to_import


def get_callable(name: Module) -> Submit:
    """returns callable"""
    try:
        return getattr(modules[name], "main")
    except:
        return getattr(modules[name], "answer")

def get_submit(path: Path) -> Submit:
    """
    returns main or answer function of given module,
    should be named submit
    """
    return get_callable(import_module(path))