class monster:
    def __init__(self) -> None:
        self.name = "Slime"

    @property
    def myname(self) -> str:
        return self.name

    @myname.setter
    def myname(self, name : str) -> None:
        self.name = name

import pytest

def test_init():
    monster1 = monster()
    assert monster1.name == "Slime"

@pytest.mark.parametrize("temp", ["small slime","red ork", "elf hunter"])
def test_get_set(temp):
    """같은 테스트를 인자만 바꿔서 여러번 해야할 때"""
    monster1 = monster()
    monster1.myname = temp
    assert monster1.myname == temp

if __name__ == "__main__":
    pytest.main()