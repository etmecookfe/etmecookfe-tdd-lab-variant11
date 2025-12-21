def count_vowels(s):
    """Counts vowels in a string."""
    # Type check
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count