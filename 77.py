# Write File
def write_file(filename, text):
  """
  Writes a line of text to a file.

  Args:
    filename: The name of the file to write to.
    text: The text to write to the file.
  """
  with open(filename, 'w') as file:
    file.write(text)

# Example usage:
user_input = input("Enter a line of text: ")
write_file("output.txt", user_input)
