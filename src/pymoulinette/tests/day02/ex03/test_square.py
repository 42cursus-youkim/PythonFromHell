answer = lambda x : x ** 2

import pytest

from random import randint

@pytest.mark.parametrize("temp", [randint(-1000000000, 1000000000) for _ in range(1000)])
def test_say_myname(temp):
    a = lambda x : x ** 2

    assert a(temp) == answer(temp)

if __name__ == "__main__":
    pytest.main()