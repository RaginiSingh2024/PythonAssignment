##Sum of List
def sum_of_list(numbers):
  """
  Calculates the sum of elements in a list.

  Args:
    numbers: The list of numbers.

  Returns:
    The sum of the elements in the list.
  """
  total = 0
  for num in numbers:
    total += num
  return total

# Example usage
my_list = [1, 2, 3, 4, 5]
list_sum = sum_of_list(my_list)
print("Sum of the list:", list_sum)