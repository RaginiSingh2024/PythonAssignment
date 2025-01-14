# Find Longest Word in File
def find_longest_word(filename):
  """
  Finds the longest word in a text file.

  Args:
    filename: The name of the file to read.

  Returns:
    The longest word in the file.
  """
  try:
    with open(filename, 'r') as file:
      longest_word = ""
      for line in file:
        words = line.split()
        for word in words:
          if len(word) > len(longest_word):
            longest_word = word
      return longest_word
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    return ""

# Example usage:
longest_word = find_longest_word("my_file.txt")
print(f"Longest word: {longest_word}")