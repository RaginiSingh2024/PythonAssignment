##String Formatting
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Using f-strings
formatted_string = f"Hello, my name is {name} and I am {age} years old."
print(formatted_string)

# Using format() method
formatted_string = "Hello, my name is {} and I am {} years old.".format(name, age)
print(formatted_string)