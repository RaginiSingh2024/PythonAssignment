 ##Simple Interest

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))

simple_interest = (principal * rate * time) / 100
print("Simple Interest:", simple_interest)