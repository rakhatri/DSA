def next_greatest_letter(letters, target):
    """
    Return the smallest character in letters that is lexicographically greater than target.

    Parameters:
    letters (List[char]): Sorted array of characters.
    target (char): The target character.

    Returns:
    char: The smallest character greater than target, or the first character if no such character exists.
    """
    # Implement the function logic
    start = 0
    end = len(letters) - 1
    while start < end:
        mid = (start + end) // 2
        if ord(letters[mid]) == ord(target):
            return letters[mid + 1]
        elif ord(letters[mid]) > ord(target):
            end = mid
        else:
            start = mid + 1
    return letters[0]


letters = ['c', 'f', 'j']
target = 'x'
print(next_greatest_letter(letters, target))

