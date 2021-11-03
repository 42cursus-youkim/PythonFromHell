class monster:
    def __init__(self) -> None:
        self.name : str = "Slime"

    def get_name(self) -> str:
        return self.name

    def set_name(self, name : str) -> None:
        self.name = name

import pytest

def test_init():
    monster1 = monster()
    assert monster1.name == "Slime"

@pytest.mark.parametrize("temp", ["small slime","red ork", "elf hunter"])
def test_get_set(temp):
    monster1 = monster()
    assert monster1.get_name() == "Slime"

    monster1.set_name(temp)
    assert monster1.get_name() == temp
    assert monster1.name == temp

if __name__ == "__main__":
    pytest.main()