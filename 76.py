# Read File
def read_file(filename):
  """
  Reads the contents of a text file and prints them to the console.

  Args:
    filename: The name of the file to read.
  """
  try:
    with open(filename, 'r') as file:
      contents = file.read()
      print(contents)
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")

# Example usage:
read_file("my_file.txt")