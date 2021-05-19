from itertools import count
from itertools import cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)


my_list = ['123', '456', '789']
iter = cycle(my_list)

n = 0
while n < 10:
    print(next(iter))
    n += 1
