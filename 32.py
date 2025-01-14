#**Fibonacci SequencePrint the first n Fibonacci numbers using iteration.
def fibonacci(n):
  """Prints the first n Fibonacci numbers using iteration."""
  a, b = 0, 1
  for i in range(n):
    print(a)
    a, b = b, a + b