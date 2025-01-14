# Flatten Nested List (Recursive)
def flatten_list(lst):
    if not lst:
        return []
    if isinstance(lst[0], list):
        return flatten_list(lst[0]) + flatten_list(lst[1:])
    else:
        return [lst[0]] + flatten_list(lst[1:])