# Reverse a list in-place (without using reversed() or slicing)

def reverse_list(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1