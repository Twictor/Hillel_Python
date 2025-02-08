zero_end = [0, 1, 0, 12, 3]
for el in zero_end:
    if el == 0:
        zero_end.remove(el)
        zero_end.append(0)
print(zero_end)