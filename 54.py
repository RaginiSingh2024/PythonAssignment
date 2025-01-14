#Count Lines in File
def count_lines(filename):
  """Reads a file and counts how many lines it contains."""
  try:
    with open(filename, 'r') as file:
      lines = file.readlines()
      return len(lines)
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    return 0

# Example usage:
line_count = count_lines("my_file.txt")
print(f"Number of lines: {line_count}")