def answer(word: str, *args: str) -> str:
    r: str = ""
    for i, j in enumerate(args):
        r += j
        if i != len(args) - 1:
            r += word
    return r


import pytest


def test_answer():
    temp = "small slime", "red ork", "elf hunter"

    assert answer(" ", "small slime", "red ork", "elf hunter") == " ".join(temp)
    assert answer("____", "small slime", "red ork", "elf hunter") == "____".join(temp)
    assert answer("\n", "small slime", "red ork", "elf hunter") == "\n".join(temp)


if __name__ == "__main__":
    pytest.main()
