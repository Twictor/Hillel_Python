pair_index = []
if not pair_index:
    print(0)
else:
    sum = 0
    for i, el in enumerate(pair_index[::2]):
        sum = sum + el
    print(sum * pair_index[-1])