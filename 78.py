# Copy File
def copy_file(source_file, destination_file):
  """
  Copies the contents of one file to another.

  Args:
    source_file: The name of the source file.
    destination_file: The name of the destination file.
  """
  try:
    with open(source_file, 'r') as source:
      with open(destination_file, 'w') as destination:
        destination.write(source.read())
  except FileNotFoundError:
    print(f"Error: Source file '{source_file}' not found.")

# Example usage:
copy_file("source.txt", "destination.txt")