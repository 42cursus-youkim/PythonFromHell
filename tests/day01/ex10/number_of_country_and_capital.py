def answer(country, capital):
    couple = sorted([[c, p] for c, p in zip(*[country, capital])], key=lambda x: x[0])
    minus = 0
    ans = {}
    for i,v in enumerate(couple):
        try:
            if ans[v[0]]:
                minus += 1
        except:
            ans[v[0]] = v[1]
            print(f"{i - minus}: {v[0]}\'s capital is {v[1]}")

# country = ['Korea','Singapore','Kenya','Iceland','France','Kenya']
# capital = ['Seoul','Singapore','Nairobi','Reykjavik','Paris','Nairobi']
# answer(country, capital)