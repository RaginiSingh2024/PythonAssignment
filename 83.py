# Search in File
def search_in_file(filename, substring):
  """
  Searches for a specific substring in a file and prints the lines where it appears.

  Args:
    filename: The name of the file to search in.
    substring: The substring to search for.
  """
  try:
    with open(filename, 'r') as file:
      for line_number, line in enumerate(file, 1):
        if substring in line:
          print(f"Line {line_number}: {line.strip()}")
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")

# Example usage:
search_in_file("my_file.txt", "search_term")