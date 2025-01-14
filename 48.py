
# Recursive Sum of List
def recursive_sum(lst):
  """Sums all elements in a list using recursion."""
  if not lst:
    return 0
  return lst[0] + recursive_sum(lst[1:])
