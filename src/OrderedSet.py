def creat():
    dic = {}
    return dic


def add(y, key, value):
    y[key] = value
    return sort(y, key)


def rem(y, key):
    del y[key]


def dec(y, key, value):
    y[key] = value
    return sort(y, key)


class OrderedSet:
    def __init__(self):
        creat()


def sort(y: dict, key):
    key1 = list(y.items())
    key2=list(y.keys())
    place = key2.index(key)
    place1 = key2.index(key) - 1
    while place1 >= 0 and y[key2[place1]] > y[key2[place]]:
        key1[place], key1[place1] = key1[place1], key1[place]
        key2[place], key2[place1] = key2[place1], key2[place]
        place1 = place1 - 1
        place = place - 1
    return dict(key1)
