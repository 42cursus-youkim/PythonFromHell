class monster:
    def __init__(self, name: str, hp: int, level: int, exp: int) -> None:
        self.name = name
        self.hp = hp
        self.level = level
        self.exp = exp

    def change_level(self, level) -> None:
        dif_level: int = level - self.level
        self.level = level
        self.hp += dif_level * 10
        if self.hp < 10:
            self.hp = 10
        self.exp += dif_level * 10
        if self.exp < 10:
            self.exp = 10


from random import randint

import pytest


@pytest.fixture
def king_monster():
    """
    동일한 함수의 결과값을 여러 번 재사용하고 싶을 때, 사용 예시:
    test_blah(cel): # 인자로 cel이 들어감
        assert cel.to_fahrenheit() == 32
    """
    return monster("king slime", 100, 999, 100)


test_monsters = [
    ["crying worms", 10, 10, 10],
    ["ork", 100, 10, 100],
    ["invisible dragon", 100000, 100000000, 100000],
]


@pytest.mark.parametrize("temp", test_monsters)
def test_init(temp):
    """같은 테스트를 인자만 바꿔서 여러번 해야할 때"""
    monster1 = monster(temp[0], temp[1], temp[2], temp[3])
    assert monster1.name == temp[0]
    assert monster1.hp == temp[1]
    assert monster1.level == temp[2]
    assert monster1.exp == temp[3]


@pytest.mark.parametrize("level", [randint(1, 1000) for _ in range(100)])
def test_change_level(level, king_monster):
    """테스트 인자 여러개일 때"""
    dif_level = level - king_monster.level
    new_hp = king_monster.hp + dif_level * 10
    new_exp = king_monster.exp + dif_level * 10
    king_monster.change_level(level)
    if new_hp < 10:
        assert king_monster.hp == 10
    else:
        assert king_monster.hp == new_hp
    if new_exp < 10:
        assert king_monster.exp == 10
    else:
        assert king_monster.exp == new_exp


if __name__ == "__main__":
    pytest.main()
