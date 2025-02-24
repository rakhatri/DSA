def generate_hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.

    Parameters:
    n (int): The size of the square.

    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    """
    # Your code here
    output = []
    # if n == 1:
    #     output.append("*" * n)
    #     return output
    output.append('*' * n)
    spaces = n - 2
    for i in range(2, n):
        output.append(f"*{' ' * spaces}*")
    output.append("*" * n)
    return output

print(generate_hollow_square(5))

