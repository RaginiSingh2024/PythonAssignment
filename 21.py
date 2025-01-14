# Find the minimum and maximum values in a list without using built-in min() or max()

def find_min_max(lst):
    if not lst:
        return None, None  # Handle empty list

    min_val = lst[0]
    max_val = lst[0]

    for num in lst:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    return min_val, max_val