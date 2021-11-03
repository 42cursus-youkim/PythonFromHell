from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from typing import Any, Callable


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


main = load_module(Path("day00/hello.py"))
main()

import pytest

# if __name__ == "__main__":
#     pytest.main(["."])
