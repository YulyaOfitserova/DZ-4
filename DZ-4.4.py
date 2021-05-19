
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

num = [my_list.count(el) for el in my_list]
el = [el for el in my_list]
new_list = [el[i] for i in range(0, len(my_list)) if num[i] == 1]

print(new_list)
