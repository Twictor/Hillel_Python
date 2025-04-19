from inspect import isgenerator


def prime_generator(end):
    prime_generators = []
    for number in range(2, end + 1):
        for prime in prime_generators:
            if not number % prime:
                break
        else:
            prime_generators.append(number)
            yield number


gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
