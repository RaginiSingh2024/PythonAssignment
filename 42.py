#Second Largest Element
def second_largest(lst):
  """Finds the second largest element in a list of unique integers."""
  if len(lst) < 2:
    return None  # Handle cases with less than two elements
  lst.sort(reverse=True)
  return lst[1]
