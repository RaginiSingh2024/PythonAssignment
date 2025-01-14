##Count Vowels
def count_vowels(s):
  """
  Counts the number of vowels (a, e, i, o, u) in a string.

  Args:
    s: The input string.

  Returns:
    The number of vowels in the string.
  """
  vowels = "aeiouAEIOU"
  count = 0
  for char in s:
    if char in vowels:
      count += 1
  return count

# Example usage
string = "Hello, how are you?"
vowel_count = count_vowels(string)
print("Number of vowels:", vowel_count)