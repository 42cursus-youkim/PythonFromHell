from importlib import import_module as _import_module
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from sys import modules
from typing import Any, Callable

Submit = Callable
Module = Any
ModuleName = str


# def import_module(path: Path) -> ModuleName:
#     """imports ModuleName by given path, keep it opened"""
#     to_import = path.stem
#     _import_module(to_import)
#     return to_import


# def get_callable(name: ModuleName) -> Submit:
#     """returns callable"""
#     try:
#         return getattr(modules[name], "main")
#     except:
#         return getattr(modules[name], "answer")


# def get_submit(path: Path) -> Submit:
#     """
#     returns main or answer function of given ModuleName,
#     should be named submit
#     """
#     return get_callable(import_module(path))


def load_module(path: Path) -> Module:
    class data:
        spec: Any = None
        module: Module = None
        loader: Any = None

    name = path.stem
    data.spec = spec_from_file_location(name, str(path))
    if data.spec:
        data.module = module_from_spec(data.spec)
    if data.module:
        data.loader = data.spec.loader
    if data.loader:
        data.loader.exec_module(data.module)
        return data.module
    raise Exception("Something went very wrong")


def load_callable(module: Module):
    """returns callable"""
    try:
        return getattr(module, "main")
    except:
        return getattr(module, "answer")


def load_submit(path: Path) -> Submit:
    """
    returns main or answer function of given ModuleName,
    should be named submit
    """
    return load_callable(load_module(path))


if __name__ == "__main__":
    ...
    # main = load_callable(load_module(Path("utils/test.py")))
    main = load_submit(Path("utils/test.py"))
    main()
    # print(modules.get("test"))
    # load_callable()
