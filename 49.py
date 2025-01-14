# GCD (Euclidean Algorithm)
def gcd(a, b):
  """Calculates the greatest common divisor of two numbers using the Euclidean algorithm."""
  while b:
    a, b = b, a % b
  return a