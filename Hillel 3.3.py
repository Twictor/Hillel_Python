checklist1 = [1, 2, 3, 4, 5, 6]
if not checklist1:
    new_list = [[], []]
    print(new_list)
elif (len(checklist1) % 2) == 0:
    split_index = len(checklist1) // 2
    new_list = [checklist1[:split_index], checklist1[split_index:]]
    print(new_list)
else:
    split_index1 = (len(checklist1) // 2) + 1
    new_list = [checklist1[:split_index1], checklist1[split_index1:]]
    print(new_list)
