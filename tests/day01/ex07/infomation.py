def answer(info):
    info_t = [tuple(person) for person in sorted(info, key=lambda x: x[0])]
    print(tuple(info_t))

# answer([['jake',184,81,4],['norman',182,86,2],['amy',157,59,1]])