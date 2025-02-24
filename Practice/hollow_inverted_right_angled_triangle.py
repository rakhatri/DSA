def generate_hollow_inverted_right_angled_triangle(n):
    """
    Function to return a hollow inverted right-angled triangle of '*' of side n as a list of strings.

    Parameters:
    n (int): The height of the triangle.

    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    output = []
    if n == 1:
        output.append('*')
        return output
    output.append('*' * n)
    for i in range(n-2, 0, -1):
        spaces = i - 1
        output.append('*' + ' ' * spaces + '*')
    output.append('*')
    return output


for elem in generate_hollow_inverted_right_angled_triangle(5):
    print(elem)
