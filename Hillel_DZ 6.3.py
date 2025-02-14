numb = int(input("Enter an integer: "))
while numb > 9:
    numb_1 = 1
    for el in str(numb):
        numb_1 *= int(el)
    numb = numb_1
print(numb)
