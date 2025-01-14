# Exception Handling
def string_to_int(string):
  """Attempts to convert a string to an integer, handling ValueError."""
  try:
    return int(string)
  except ValueError:
    print("Error: Could not convert string to integer.")
    return None

# Example usage:
result = string_to_int("123") 
print(result) 
result = string_to_int("abc")