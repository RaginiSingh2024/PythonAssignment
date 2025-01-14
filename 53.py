#File Copy
def copy_file(source_file, destination_file):
  """Copies the contents of one text file to another."""
  try:
    with open(source_file, 'r') as source:
      with open(destination_file, 'w') as destination:
        destination.write(source.read())
    print(f"File '{source_file}' copied to '{destination_file}' successfully.")
  except FileNotFoundError:
    print(f"Error: Source file '{source_file}' not found.")
  except IOError:
    print(f"Error: Could not write to destination file '{destination_file}'.")

# Example usage:
copy_file("source.txt", "destination.txt")