
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

el = [el for el in my_list]
elements = [el[i] for i in range(1, len(my_list)) if el[i] > el[i - 1]]

print(f'Исходный список: {my_list}')
print(f'Новый список: {elements}')
