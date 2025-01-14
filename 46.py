# Frequency of Elements
def count_frequencies(lst):
  """Counts how often each element appears in a list and stores the result in a dictionary."""
  freq_dict = {}
  for item in lst:
    freq_dict[item] = freq_dict.get(item, 0) + 1
  return freq_dict