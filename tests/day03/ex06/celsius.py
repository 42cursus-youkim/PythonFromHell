class Celsius:
    def __init__(self, temperature: int = 4) -> None:
        self._temperature: int = temperature

    def to_fahrenheit(self) -> int:
        return int(self._temperature * 1.8 + 32)

    @property
    def temperature(self) -> int:
        print("get value")
        return self._temperature

    @temperature.setter
    def temperature(self, value: int):
        if value < -273:
            raise ValueError("Temperature can't be lower than absolute zero!")
        print("set value")
        self._temperature = value


from random import randint

import pytest


@pytest.fixture
def cel():
    """
    동일한 함수의 결과값을 여러 번 재사용하고 싶을 때, 사용 예시:
    test_blah(cel): # 인자로 cel이 들어감
        assert cel.to_fahrenheit() == 32
    """
    return Celsius(0)


@pytest.mark.parametrize("temp", [randint(-273, 999) for _ in range(20)])
def test_get_set(temp):
    """같은 테스트를 인자만 바꿔서 여러번 해야할 때"""
    cel = Celsius(temp)
    assert cel.temperature == temp


@pytest.mark.parametrize("temp, expected", [(0, 32), (37, 98), (100, 212)])
def test_fahrenheit(temp, expected):
    """테스트 인자 여러개일 때"""
    assert Celsius(temp).to_fahrenheit() == expected


@pytest.mark.parametrize("temp", [randint(-273, 999) for _ in range(20)])
def test_set(cel, temp):
    cel.temperature = temp
    assert cel.temperature == temp


def test_set_exception():
    """예외가 일어나는지 확인해야 할때"""
    with pytest.raises(ValueError):
        Celsius().temperature = -700


if __name__ == "__main__":
    pytest.main()
# c = Celsius()
# print("----------")
# print(c._temperature)
# print("----------")
# print(c.to_fahrenheit())
# print("----------")
# c.temperature = 300
# print("----------")
# c.temperature = -700
