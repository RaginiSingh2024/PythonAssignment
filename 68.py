# Power Function
def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp-1)