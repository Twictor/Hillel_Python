import random

random_list = []
range_list = random.randint(3, 10)
n = 0
while n != range_list:
    random_list.append(random.randint(1, 10))
    n = n + 1
new_random = [random_list[0], random_list[2], random_list[-2]]
print(random_list, " = ", new_random)
