def is_perfect_square(num):
    """
    Function to check if a number is a perfect square.

    Parameters:
    num (int): The number to check.

    Returns:
    bool: True if num is a perfect square, False otherwise.
    """
    # Your code here
    i = 1

    while i <= int(num ** 0.5):
        if i * i == num:
            return True
        i += 1
    return False

print(is_perfect_square(16))