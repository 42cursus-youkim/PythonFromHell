from balance import monster

class slime(monster):
    def __init__(self, name: str, hp: int, level: int, exp: int) -> None:
        super().__init__(name, hp, level, exp)
        self._atk = 50
    
    @property
    def atk(self):
        return self._atk
    
    @atk.setter
    def atk(self, atk):
        if atk < 0:
            raise ValueError("atk error")
        self._atk = atk
    
    def change_level(self, level) -> None:
        dif_level: int = level - self.level
        super().change_level(level)
        new_atk = self._atk + dif_level*5
        if new_atk < 0:
            raise ValueError("atk error")
        self._atk = new_atk

from random import randint

import pytest


@pytest.fixture
def king_slime():
    """
    동일한 함수의 결과값을 여러 번 재사용하고 싶을 때, 사용 예시:
    test_blah(cel): # 인자로 cel이 들어감
        assert cel.to_fahrenheit() == 32
    """
    return slime("king slime", 1000, 999, 1000)

test_slimes = [
    ["king slime", 10000, 999, 10000],
    ["slime", 100, 10, 100],
    ["yellow slime", 1000, 300, 1000],
]

@pytest.mark.parametrize("temp", test_slimes)
def test_init(temp):
    """같은 테스트를 인자만 바꿔서 여러번 해야할 때"""
    slime1 = slime(temp[0],temp[1],temp[2],temp[3])
    assert slime1.name == temp[0]
    assert slime1.hp == temp[1]
    assert slime1.level == temp[2]
    assert slime1.exp == temp[3]
    assert slime1.atk == 50

@pytest.mark.parametrize("temp", [randint(-1000, 1000) for _ in range(10)])
def test_get_set(temp, king_slime):
    """같은 테스트를 인자만 바꿔서 여러번 해야할 때"""
    if temp < 0:
        with pytest.raises(ValueError):
            king_slime.atk = temp
    else:
        king_slime.atk = temp
        assert king_slime.atk == temp

@pytest.mark.parametrize("level", [randint(1, 1000) for _ in range(10)])
def test_change_level(level, king_slime):
    """테스트 인자 여러개일 때"""
    dif_level = level - king_slime.level
    new_atk = king_slime.atk + dif_level*5
    if new_atk < 0:
        with pytest.raises(ValueError):
            king_slime.change_level(level)
    else:
        king_slime.change_level(level)
        assert king_slime.atk == new_atk


if __name__ == "__main__":
    pytest.main()