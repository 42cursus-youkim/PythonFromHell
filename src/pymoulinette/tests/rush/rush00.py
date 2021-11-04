def answer(input_num):
    roman_word = ["Ⅰ", "Ⅴ", "Ⅹ", "Ⅼ", "Ⅽ", "Ⅾ", "Ⅿ"]
    number_word = [1, 5, 10, 50, 100, 500, 1000]
    roman_word_dict = {key: value for key, value in zip(*[number_word, roman_word])}
    converted_roman_num = ""
    if input_num > 1000 and input_num <= 0:
        return ValueError
    while input_num != 0:
        for number in number_word[::-1]:
            if input_num >= number:
                input_num -= number
                converted_roman_num += roman_word_dict[number]
                break
    return converted_roman_num


# answer(123)

# def submit(input_num):
#     roman_word = ['Ⅰ', 'Ⅴ', 'Ⅹ', 'Ⅼ', 'Ⅽ', 'Ⅾ', 'Ⅿ']
#     number_word = [1, 5, 10, 50, 100, 500, 1000]
#     roman_word_dict = {key : value for key, value in zip(*[number_word, roman_word])}
#     converted_roman_num = ""
#     if input_num > 1000:
#         return ValueError
#     while input_num != 0:
#         for number in number_word[::-1]:
#             if input_num >= number:
#                 input_num -= number
#                 converted_roman_num += roman_word_dict[number]
#                 break
#     return converted_roman_num

from random import randint

import pytest

param = [randint(0, 1000) for _ in range(20)]


@pytest.mark.parametrize("num", param)
def test_get_set(num):
    assert answer(num) == submit(num)


if __name__ == "__main__":
    pytest.main()
