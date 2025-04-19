user = int(input("Enter a 5-digit number: "))
num0 = user // 10000
user1 = user - (num0 * 10000)
num1 = user1 // 1000
user2 = user1 - (num1 * 1000)
num2 = user2 // 100
user3 = user2 - (num2 * 100)
num3 = user3 // 10
num4 = user3 - (num3 * 10)
print(num4 * 10000 + num3 * 1000 + num2 * 100 + num1 * 10 + num0)