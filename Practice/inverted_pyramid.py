def generate_inverted_pyramid(n):
    """
    Function to return an inverted pyramid pattern of '*' of side n as a list of strings.

    Parameters:
    n (int): The number of rows in the inverted pyramid.

    Returns:
    list: A list of strings where each string represents a row of the inverted pyramid.
    """
    # Your code here
    output = []
    for i in range(n, 0, -1):
        stars = 2 * i - 1
        spaces = n - i
        output.append(' ' * spaces + '*' * stars + ' ' * spaces)
    return output


for elem in generate_inverted_pyramid(5):
    print(elem)