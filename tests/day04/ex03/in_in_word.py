def answer(string, word):
    word_lst = string.split(' ')
    lst = list(map(lambda x : x.lower() if word in x else x.upper(), word_lst))
    return lst

# string = "Hello welcome to Python World!"
# word = "l"
# print(answer(string, word))