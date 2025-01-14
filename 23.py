# Count Occurrences in List

def count_occurrences(lst, target):
    count = 0
    for num in lst:
        if num == target:
            count += 1
    return count