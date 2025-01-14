#Find & Replace in File
def replace_in_file(filename, old_word, new_word):
  """Searches for a specific word in a file and replaces it with another word."""
  try:
    with open(filename, 'r+') as file:
      text = file.read()
      new_text = text.replace(old_word, new_word)
      file.seek(0)
      file.write(new_text)
      file.truncate()
    print(f"Replaced '{old_word}' with '{new_word}' in '{filename}'.")
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")

# Example usage:
replace_in_file("my_file.txt", "old_word", "new_word")