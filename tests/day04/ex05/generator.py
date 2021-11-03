from math import ceil

def geneclass(n1, n2):
    for num in range(n1, n2 + 1):
        if (num % 2):
            yield num
        else:
            pass

# n1 = 1
# n2 = 9
# g = geneclass(n1, n2)
# for i in range(ceil((n2 - n1 + 1)/2)):
#     print(next(g))