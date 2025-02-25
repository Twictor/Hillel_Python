def difference(*args):
    if not args:
        return 0
    max_set = max(args)
    min_set = min(args)
    result = max_set - min_set
    return round(result, 2)


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
