nums = [12, 3, 4, 10]
if nums == []:
    print(nums)
else:
    range_of_nums = len(nums) - 1
    value = nums[range_of_nums]
    nums.insert(0, value)
    nums.pop()
    print(nums)
