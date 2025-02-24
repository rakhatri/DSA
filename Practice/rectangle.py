def generate_rectangle(n, m):
    """
    Function to return a rectangle pattern of '*' with length n and breadth m as a list of strings.

    Parameters:
    n (int): The number of rows in the rectangle.
    m (int): The number of columns in the rectangle.

    Returns:
    list: A list of strings where each string represents a row of the rectangle pattern.
    """
    output = []
    for i in range(n):
        output.append('*' * m)
    return output

print(generate_rectangle(3, 2))