def generate_sandglass(n):
    """
    Function to return a sandglass pattern of '*' of side n as a list of strings.

    Parameters:
    n (int): The height of the sandglass.

    Returns:
    list: A list of strings where each string represents a row of the sandglass pattern.
    """
    # Your code here
    output = []
    for i in range(n, 1, -1):
        spaces = n - i
        stars = 2 * i - 1
        output.append(' ' * spaces + '*' * stars + ' ' * spaces)
    for i in range(1, n+1):
        spaces = n - i
        stars = 2 * i - 1
        output.append(' ' * spaces + '*' * stars + ' ' * spaces)
    return output


for elem in generate_sandglass(5):
    print(elem)
