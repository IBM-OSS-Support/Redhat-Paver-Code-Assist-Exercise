def count_vowels(s):
    vowels = 'aeiou'  # Step 1: Define a string containing all vowels.
    return sum(1 for char in s.lower() if char in vowels)  # Step 2: Count the vowels.

