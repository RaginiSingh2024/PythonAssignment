#Invert Dictionary
def invert_dict(d):
  """Inverts a dictionary (keys become values, values become keys)."""
  return {v: k for k, v in d.items()}
