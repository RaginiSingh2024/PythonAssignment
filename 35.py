#Palindrome Check (Number)
def is_palindrome(num):
  """Checks if a number is a palindrome."""
  temp = num
  reverse = 0
  while temp > 0:
    last_digit = temp % 10
    reverse = (reverse * 10) + last_digit
    temp //= 10
  return num == reverse

import random