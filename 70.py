# Binary Search (Recursive)
def binary_search(lst, target, low, high):
    if low > high:
        return -1  # Not found
    mid = (low + high) // 2
    if lst[mid] == target:
        return mid
    elif target < lst[mid]:
        return binary_search(lst, target, low, mid-1)
    else:
        return binary_search(lst, target, mid+1, high)
