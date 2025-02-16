import string

span = input("Введіть через дефіс дві літери: ")
start = string.ascii_letters.index(span[0])
end = string.ascii_letters.index(span[2])
if start > end:
    start, end = end, start
for el in string.ascii_letters:
    if start <= string.ascii_letters.index(el) <= end:
        print(el, end="")
