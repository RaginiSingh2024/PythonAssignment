# Handle File Exceptions
def read_file_with_exception_handling(filename):
  """
  Reads the contents of a text file and prints them to the console,
  handling potential exceptions (e.g., FileNotFoundError).

  Args:
    filename: The name of the file to read.
  """
  try:
    with open(filename, 'r') as file:
      contents = file.read()
      print(contents)
  except FileNotFoundError as e:
    print(f"Error: {e}")

# Example usage:
read_file_with_exception_handling("my_file.txt")