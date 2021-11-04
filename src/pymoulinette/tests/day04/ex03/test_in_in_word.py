def answer(string, word):
    word_lst = string.split(' ')
    lst = list(map(lambda x : x.lower() if word in x else x.upper(), word_lst))
    return lst

def submit(string, word):
    word_lst = string.split(' ')
    lst = list(map(lambda x : x.lower() if word in x else x.upper(), word_lst))
    return lst

# string = "Hello welcome to Python World!"
# word = "l"
# print(answer(string, word))

from random import randint
import pytest

string_lst = ["It is kind of fun to do the impossible",
                "There are better starters than me but Im a strong finisher",
                "Tough times never last but tough people do",
                "Grind Hard Shine Hard"]
word_set = []
word_lst = []
for idx, word in enumerate(string_lst):
    word_set.append(list(set(word)))
    word_set[idx].remove(' ')
    word_lst.append(word_set[idx][randint(0, len(word_set[idx]))])
@pytest.mark.parametrize("string, word", [[string, word] for string, word in zip(*[string_lst, word_lst])])
def test_get_set(string, word):
    assert answer(string, word) == submit(string, word)

if __name__ == "__main__":
    pytest.main()