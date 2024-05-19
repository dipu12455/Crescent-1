import random

list = [0]
number = 0
for i in range(0, 50):
    while number in list:
        number = random.randint(0,9999)
    list.append(number)
print(list)