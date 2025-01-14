# Line Count
def line_count(filename):
  """
  Counts the number of lines in a file.

  Args:
    filename: The name of the file to read.

  Returns:
    The number of lines in the file.
  """
  try:
    with open(filename, 'r') as file:
      line_count = 0
      for line in file:
        line_count += 1
      return line_count
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    return 0

# Example usage:
line_count = line_count("my_file.txt")
print(f"Number of lines: {line_count}")