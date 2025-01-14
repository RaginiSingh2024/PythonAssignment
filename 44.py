#Dictionary of Squares
n = int(input("Enter a value for n: "))
squares_dict = {i: i**2 for i in range(1, n+1)}
print("Dictionary of squares:", squares_dict)