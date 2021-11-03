def answer(country, capital):
    couple = sorted([[c, p] for c, p in zip(*[country, capital])], key=lambda x: x[0])
    ans = {}
    for cou, cap in couple:
        try:
            ans[cou] = cap
        except:
            pass
    print(ans)

# country = ['korea','Singapore','Kenya','Iceland','France','Kenya']
# capital = ['Seoul','Singapore','Nairobi','Reykjavik','Paris','Nairobi']
# answer(country, capital)