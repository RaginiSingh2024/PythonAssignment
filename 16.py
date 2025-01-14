## Power Calculation
def power(base, exponent):
  """
  Calculates base raised to the power of exponent.

  Args:
    base: The base number.
    exponent: The exponent.

  Returns:
    The result of base raised to the power of exponent.
  """
  if exponent == 0:
    return 1
  result = 1
  for _ in range(exponent):
    result *= base
  return result

# Example usage
base = 2
exponent = 3
result = power(base, exponent)
print(base, "raised to the power of", exponent, "is:", result)