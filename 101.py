# Use Random Module
import random

def random_choice(lst):
  """Randomly selects an element from a given list."""
  return random.choice(lst)

my_list = [1, 2, 3, 4, 5]
random_element = random_choice(my_list)
print(random_element)