def answer(word: str, *args: str) -> str:
    r: str = ""
    for i, j in enumerate(args):
        r += j
        if i != len(args) - 1:
            r += word
    return r
