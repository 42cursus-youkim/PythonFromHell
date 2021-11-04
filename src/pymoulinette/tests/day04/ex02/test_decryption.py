def answer(str1, str2):
    lst = [str1, str2]
    ans = ""
    for word in zip(*lst):
        ans = ans + word[0]
        ans = ans + word[-1]
    print(ans)

def submit(str1, str2):
    lst = [str1, str2]
    ans = ""
    for word in zip(*lst):
        ans = ans + word[0]
        ans = ans + word[-1]
    print(ans)

# str1 = "오 시북쪽로기대 전라"
# str2 = "후3 동으 병를출하!"
# print(answer(str1, str2))


from random import randint

import pytest

str1_lst = ["오 시북쪽로기대 전라", "배 격 행다", "밀는본뒤먹 에."]
str2_lst = ["후3 동으 병를출하!", "벽공을강한!", "서   어없라"]
@pytest.mark.parametrize("str1, str2", [[str1, str2] for str1, str2 in zip(*[str1_lst, str2_lst])])
def test_get_set(str1, str2):
    assert answer(str1, str2) == submit(str1, str2)

if __name__ == "__main__":
    pytest.main()