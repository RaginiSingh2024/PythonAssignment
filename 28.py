# Sum of Digits

num_str = input("Enter a number (as a string): ")
total = 0
for digit in num_str:
    total += int(digit)
print("Sum of digits:", total)