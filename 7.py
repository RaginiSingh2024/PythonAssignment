7. ##Largest of Three


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

largest = num1

if num2 > largest:
    largest = num2

if num3 > largest:
    largest = num3

print("The largest number is:", largest)