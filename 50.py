# LCM
def lcm(a, b):
  """Calculates the least common multiple of two numbers using the GCD."""
  return (a * b) // gcd(a, b)
