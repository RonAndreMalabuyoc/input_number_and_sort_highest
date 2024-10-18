num1 = int(input("Enter the first number here: "))
num2 = int(input("Enter the second number here: "))
num3 = int(input("Enter the third number here: "))
num4 = int(input("Enter the forth number here: "))
num5 = int(input("Enter the fifth number here: "))

highest = num1

if num2 > highest:
    highest = num2

if num3 > highest:
    highest = num3

if num4 > highest:
    highest = num4

if num5 > highest:
    highest = num5


print("The highest number is:", highest)