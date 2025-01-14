# Count Vowels (Recursive)
def count_vowels(s):
    vowels = "aeiouAEIOU"
    if not s:
        return 0
    else:
        return (1 if s[0] in vowels else 0) + count_vowels(s[1:])