def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Returns True if ransomNote can be constructed from magazine,
    where each letter in magazine can only be used once.
    Uses a dictionary (hash table) for frequency counting.
    """
    # Step 1: Count letters in magazine
    letter_counts = {}
    for char in magazine:
        letter_counts[char] = letter_counts.get(char, 0) + 1

    # Step 2: Check ransomNote requirements
    for char in ransomNote:
        if char not in letter_counts or letter_counts[char] == 0:
            return False
        letter_counts[char] -= 1

    return True
