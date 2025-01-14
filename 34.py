#prime check
def prime_numbers_in_range(start, end):
  """Displays all prime numbers between two integers start and end."""
  for num in range(start, end + 1):
    if is_prime(num):
      print(num)