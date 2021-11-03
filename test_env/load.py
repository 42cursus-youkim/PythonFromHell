from pathlib import Path
from typing import Any, Callable

from utils import load_module

main = load_module(Path("day00/hello.py"))
main()

import pytest

if __name__ == "__main__":
    pytest.main(["."])
