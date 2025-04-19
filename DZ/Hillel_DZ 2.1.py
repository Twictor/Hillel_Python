user = int(input("Enter a 4-digit number: "))
num1 = user // 1000
print('num1: ', num1)
user2 = user - (num1 * 1000)
num2 = user2 // 100
print('num2: ', num2)
user3 = user2 - (num2 * 100)
num3 = user3 // 10
print('num3: ', num3)
num4 = user3 - (num3 * 10)
print('num4: ', num4)