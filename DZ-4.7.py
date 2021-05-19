
def fact():
    n = 10
    i = 1
    res = 1
    while i < n:
        res = res * i
        i += 1
        yield res

for el in fact():
    print(el)
    