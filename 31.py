##Factorial Using For Loop**
Calculate the factorial of a number using a for loop.

def factorial(n):
  """Calculates the factorial of a number using a for loop."""
  if n == 0:
    return 1
  result = 1
  for i in range(1, n + 1):
    result *= i
  return result