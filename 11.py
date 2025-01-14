
def string_length(s):
  """
  Returns the length of a string without using the built-in len() function.

  Args:
    s: The input string.

  Returns:
    The length of the string.
  """
  count = 0
  for _ in s:
    count += 1
  return count

# Example usage
my_string = "Hello"
length = string_length(my_string)
print("Length of", my_string, "is:", length)