my_list = [0, 2, 5, 4, 5, 9, 78, 1, 2, 3]
new_list = [el for el in my_list if el > my_list[my_list.index(el)-1]]
print(new_list)
