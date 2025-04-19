import string
import keyword

line = input("Enter your variable name: ")
eror_line = 0

if line.count("__") or line.count("___"):
    print(False)
elif line[0] == ("_"):
    print(True)
else:
    if line[0].isdigit():
        print(False)
    elif line.isspace():
        print(False)
    elif not line.islower():
        print(False)
    else:
        for el in line:
            for symb in string.punctuation:
                if symb == "_":
                    continue
                elif el == symb or el == " ":
                    eror_line += 1
        if eror_line > 0:
            print(False)
        elif line in keyword.kwlist:
            print(False)
        else:
            print(True)
