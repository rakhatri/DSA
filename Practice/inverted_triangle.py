def generate_inverted_triangle(n):
    """
    Function to return an inverted right-angled triangle of '*' of side n as a list of strings.

    Parameters:
    n (int): The height and base of the triangle.

    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    output = []
    for i in range(n, 0, -1):
        output.append('*' * i)
    return output


print(generate_inverted_triangle(5))
