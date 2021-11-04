def answer(info):
    for i, v in enumerate(info):
        if len(v) != 4:
            del info[i]
    info_t = [tuple(person) for person in sorted(info, key=lambda x: x[0])]
    return tuple(info_t)


def submit(info):
    for i, v in enumerate(info):
        if len(v) != 4:
            del info[i]
    info_t = [tuple(person) for person in sorted(info, key=lambda x: x[0])]
    return tuple(info_t)


# answer([['jake',184,81,4],['norman',182,86,2],['amy',157,59,1]])

from random import randint

import pytest

name = [
    "Liam",
    "Olivia",
    "Noah",
    "Emma",
    "Oliver",
    "Ava",
    "Elijah",
    "Charlotte",
    "William",
    "Sophia",
    "James",
    "Amelia",
    "Benjamin",
    "Isabella",
    "Lucas",
    "Mia",
    "Henry",
    "Evelyn",
    "Alexander",
    "Harper",
]

param = []
for _ in range(8):
    param.append(
        [name[randint(0, 19)], randint(140, 190), randint(40, 120), randint(1, 4)]
    )


@pytest.mark.parametrize("temp", [[param] for _ in range(6)])
def test_get_set(temp):
    assert answer(temp) == submit(temp)


if __name__ == "__main__":
    pytest.main()
