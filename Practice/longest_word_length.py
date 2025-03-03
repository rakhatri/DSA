def longest_word_length(s):
    """
    Function to find the length of the longest word in a string without using built-in functions.

    Parameters:
    s (str): The input string.

    Returns:
    int: The length of the longest word.
    """
    # Your code here
    max_word = 0
    in_word = False
    i = 0
    count = 0
    while i < len(s):
        if s[i] == " ":
            count = 0
            if not in_word:
                in_word = True
        else:
            count += 1
            if count > max_word:
                max_word = count
        i += 1
    return max_word

print(longest_word_length("Helloss worlds"))
