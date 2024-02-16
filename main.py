result = []

def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a / b




try:
    data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}
    res = divider(key, data[key])
except SyntaxError as sn:
    print(sn)
except TypeError as tp:
    data = {10: 2, 2: 5, "123": 4, 18: 0, "GGG": 15, 8: 4}
    print(tp)
except NameError as nm:
    res = divider(key, data[key])
    result.append(res)
    print(nm)
except ValueError as vl:
    a = 5
    b = 101
    result.append(res)
    print(vl)






print(result)