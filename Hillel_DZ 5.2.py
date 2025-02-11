while True:
    num1 = input("Enter first number: ")
    symb = input("Enter the symbol: +, -, *, / ")
    num2 = input("Enter second number: ")

    if not num1.isdigit() or not num2.isdigit():
        print("Incorect data")
    elif symb == '+':
        resultat = int(num1) + int(num2)
        print("resultat = ", resultat)
    elif symb == '-':
        resultat = int(num1) - int(num2)
        print("resultat = ", resultat)
    elif symb == '*':
        resultat = int(num1) * int(num2)
        print("resultat = ", resultat)
    elif symb == '/':
        if num2 != '0':
            resultat = int(num1) // int(num2)
            print("resultat = ", resultat)
        else:
            print("Error you can't divide by '0'")
    choice_1 = input("If you want to continue, enter y or yes: ")
    if choice_1 not in ['y', 'yes']:
        print("Calculator stopped ")
        break
