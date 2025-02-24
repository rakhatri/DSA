def generate_number_pyramid(n):
    """
    Function to return a pyramid pattern of numbers of height n as a list of strings.

    Parameters:
    n (int): The height of the pyramid.

    Returns:
    list: A list of strings where each string represents a row of the pyramid pattern.
    """
    # Your code here
    current_number = 1
    output = []

    for i in range(1, n+1):
        space = n - i
        row = ' '.join(str(current_number + j) for j in range(i))
        row = ' ' * space + row + ' ' * space
        output.append(row)
        current_number = 1
    return output


for elem in generate_number_pyramid(5):
    print(elem)