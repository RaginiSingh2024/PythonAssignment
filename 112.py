# Filter & Reduce
from functools import reduce

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
sum_of_evens = reduce(lambda x, y: x + y, even_numbers)
print(sum_of_evens)