## Check Palindrome
def is_palindrome(s):
  """
  Checks if a given string is a palindrome.

  Args:
    s: The input string.

  Returns:
    True if the string is a palindrome, False otherwise.
  """
  s = s.lower()  # Convert to lowercase to handle case-insensitive palindromes
  return s == s[::-1]  # Compare the string with its reversed version

# Example usage
string = input("Enter a string: ")
if is_palindrome(string):
  print(string, "is a palindrome.")
else:
  print(string, "is not a palindrome.")