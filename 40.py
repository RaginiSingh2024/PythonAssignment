#Binary Search (Iterative)
def binary_search(arr, x):
  """Performs iterative binary search."""
  low = 0
  high = len(arr) - 1
  while low <= high:
    mid = (high + low) // 2
    if arr[mid] < x:
      low = mid + 1
    elif arr[mid] > x:
      high = mid - 1
    else:
      return mid
  return -1  # If the element is not found