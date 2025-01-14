# Append to File
def append_to_file(filename, text):
  """
  Appends a line of text to an existing file without overwriting it.

  Args:
    filename: The name of the file to append to.
    text: The text to append to the file.
  """
  with open(filename, 'a') as file:
    file.write(text + '\n')

# Example usage:
user_input = input("Enter a line of text to append: ")
append_to_file("my_file.txt", user_input)