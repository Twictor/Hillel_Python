def common_elements():
    list_1 = []
    list_2 = []
    for el in range(0, 100):
        if el % 3 == 0:
            list_1.append(el)
    for el in range(0, 100):
        if el % 5 == 0:
            list_2.append(el)
    return set(list_1).intersection(set(list_2))


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ОК')