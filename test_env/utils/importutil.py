from importlib import import_module as _import_module
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from sys import modules
from typing import Any, Callable

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


def load_module(path: Path) -> Callable:
    class data:
        spec: Any = None
        module: Any = None
        loader: Any = None

    data.spec = spec_from_file_location(path.stem, str(path))
    if data.spec:
        data.module = module_from_spec(data.spec)
    if data.module:
        data.loader = data.spec.loader
    if data.loader:
        data.loader.exec_module(data.module)
        main: Callable = getattr(data.module, "main")
        return main
    raise Exception("No main function found")
