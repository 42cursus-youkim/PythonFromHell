from typing import Dict, List, Any


def answer(list_monster : List[Dict[str, Any]]):
    return list(filter(lambda x : x['level'] >= 20, list_monster))


import pytest

list_monster = [
    [
    {'name' : 'ork', 'hp' : 100, 'level' : 20},
    {'name' : 'invisible dragon', 'hp' : 200, 'level' : 30},
    {'name' : 'crazy slime', 'hp' : 300, 'level' : 10},
    {'name' : 'king rabbit', 'hp' : 400, 'level' : 210}
    ],
    [
    {'name' : 'crazy slime', 'hp' : 300, 'level' : 10},
    {'name' : 'king rabbit', 'hp' : 400, 'level' : 210}
    ],
    []
]

@pytest.mark.parametrize("temp", list_monster)
def test_say_myname(temp):
    a = list(filter(lambda x : x['level'] >= 20, temp))

    assert a == answer(temp)

if __name__ == "__main__":
    pytest.main()