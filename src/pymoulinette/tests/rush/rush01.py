from itertools import permutations

def check_answer(word_dict, lst, ans):
    compress = [ele for ele in lst]
    compress.append(ans)
    word_scores = []
    for word in compress:
        word_score = 0
        for alphabet in word:
            word_score = word_score * 10 + word_dict[alphabet]
        word_scores.append(word_score)
    if sum(word_scores[:-1]) == word_scores[-1]:
        return True
    else:
        return False

def answer(lst, ans):
    compress = [ele for ele in lst]
    compress.append(ans)
    spelling = ''
    for word in compress:
        spelling += word
    spelling = set(spelling)
    if len(spelling) > 10:
        return ValueError
    word_scores = []
    for permuate in permutations(range(0, 10), len(spelling)):
        word_dict = {k:v for k,v in zip(*[spelling, permuate])}
        if check_answer(word_dict, lst, ans):
            return word_dict
        else:
            word_scores = []


# lst = ['SEND', 'MORE']
# ans = 'MONEY'
# print(answer(lst, ans))

lst_lst = [["PLAY", "THE"], ["BEAT", "THE"], ["ONE", "TWO", "FOUR"],
            ["ALL", "COWS", "EAT"], ["SEVEN", "SEVEN", "SIX"],
            ["APPLE", "GRAPE", "PLUM"], ["ONE", "THREE", "FOUR"],["HEART", "MYTH"]]
ans_lst = ["GAME","DRUM","SEVEN","GRASS","TWENTY","BANANA","EIGHT","RHYME"]

from random import randint

import pytest


idx = randint(0, len(ans_lst))
param = [[lst_lst[idx], ans_lst[idx]] for idx in range(len(ans_lst))]
@pytest.mark.parametrize("lst, ans", param)
def test_get_set(lst, ans):
    word_dict = answer(lst, ans)
    assert check_answer(word_dict, lst, ans) == True

if __name__ == "__main__":
    pytest.main()