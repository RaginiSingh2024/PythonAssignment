#Word Count in File
def word_count(filename):
  """
  Counts the number of words in a file.

  Args:
    filename: The name of the file to read.

  Returns:
    The number of words in the file.
  """
  try:
    with open(filename, 'r') as file:
      text = file.read()
      words = text.split()
      return len(words)
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    return 0

# Example usage:
word_count = word_count("my_file.txt")
print(f"Number of words: {word_count}")