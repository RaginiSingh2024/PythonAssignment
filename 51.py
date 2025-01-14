#File Read
def read_file(filename):
  """Reads a text file and prints its contents to the screen."""
  try:
    with open(filename, 'r') as file:
      contents = file.read()
      print(contents)
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")

# Example usage:
read_file("my_file.txt")