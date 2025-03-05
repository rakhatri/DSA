def generate(numRows):
    """
    Function to generate the first numRows of Pascal's triangle.
    :param numRows: int -> Number of rows of Pascal's triangle to generate
    :return: List[List[int]] -> The first numRows of Pascal's triangle
    """
    triangle = []

    for row_num in range(numRows):
        row = [1] * (row_num + 1)
        for j in range(1, row_num):
            row[j] = triangle[row_num - 1][j-1] + triangle[row_num - 1][j]
        triangle.append(row)
    return triangle


triangle = generate(5)
for elem in triangle:
    print(elem)



