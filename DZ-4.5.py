from functools import reduce

def comp(prev_el, el):
    return prev_el * el

print(reduce(comp, range(100, 1001, 2)))
