def get_next_line(f, bytesize = 1024):
    res = ''
    while (lines := f.read(bytesize)) != '':
        res += lines
        while '\n' in res:
            idx = res.find('\n')
            yield res[:idx]
            res = res[idx+1:]
    yield res
    f.close()

def open_file(file_name):
    f = open(file_name,'r')
    return f

# import os
# base_path = os.getcwd()
# target_path = "/hacker_ton/text.txt"

# f = open_file(base_path + target_path)

# for line in get_next_line(f):
#     print(line)