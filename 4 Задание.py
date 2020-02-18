my_list = [1, 2, 4, 6, 2, 5, 2, 9, 0]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)