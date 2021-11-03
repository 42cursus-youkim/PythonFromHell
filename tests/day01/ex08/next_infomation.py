def answer(info, info_news):
    ans = [tuple(person) for person in info_news]
    for person in info:
        person_lst = list(person)
        person_lst[-1] += 1
        if not person_lst[-1] >= 5:
            ans.append(tuple(person_lst))
    print(sorted(ans, key=lambda x: x[0]))


# info = (('amy', 157, 59, 1), ('jake', 184, 81, 4), ('norman', 182, 86, 2))
# info_news = [['rachel',178,63,1]]
# answer(info, info_news)