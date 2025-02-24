def generate_pyramid(n):
    """
    Function to return a pyramid pattern of '*' of side n as a list of strings.

    Parameters:
    n (int): The number of rows in the pyramid.

    Returns:
    list: A list of strings where each string represents a row of the pyramid.
    """
    # Your code here
    output = []
    for i in range(1, n+1):
        stars = 2 * i - 1
        spaces = n - i
        output.append(' ' * spaces + '*' * stars + ' ' * spaces)
    return output


for elem in generate_pyramid(5):
    print(elem)
