namber = [el for el in range(20,241)]
new_namer = [el for el in namber if el % 20 == 0 or el % 21 == 0]
print(new_namer)