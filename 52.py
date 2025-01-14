#File Write
def write_to_file(filename, text):
  """Prompts the user for a string and writes it to a new text file."""
  try:
    with open(filename, 'w') as file:
      file.write(text)
    print(f"Text written to '{filename}' successfully.")
  except IOError:
    print(f"Error: Could not write to file '{filename}'.")

# Example usage:
user_input = input("Enter text to write: ")
write_to_file("new_file.txt", user_input)