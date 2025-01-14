## Compound Interest
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))

compound_interest = principal * (pow((1 + rate/100), time) - 1)
print("Compound Interest:", compound_interest)