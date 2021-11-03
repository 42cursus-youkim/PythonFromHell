def answer(num_lst):
    num_lst_edit = [num*3 for num in num_lst]
    num_lst = [num[:int(len(num)/3)] for num in sorted(num_lst_edit, reverse=True)]
    number = ""
    for num in num_lst:
        number += num
    print(number)

# num_lst = ["3", "300", "303", "9"]
# answer(num_lst)