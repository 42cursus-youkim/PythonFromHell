class monster:
    def __init__(self, name : str) -> None:
        self.name: str = name

    def say_myname(self) -> None:
        print(self.name)

import pytest

monster_names = ["small slime","red ork", "elf hunter"]

@pytest.mark.parametrize("temp", monster_names)
def test_init(temp):
    monster1 = monster(temp)
    assert monster1.name == temp

@pytest.mark.parametrize("temp", monster_names)
def test_say_myname(temp, capsys):
    monster1 = monster(temp)
    monster1.say_myname()

    assert capsys.readouterr().out == "{}\n".format(temp)

if __name__ == "__main__":
    pytest.main()