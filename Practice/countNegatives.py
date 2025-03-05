def countNegatives(grid):
    # Implement your solution here
    def countNegativesInRow(row):
        left = 0
        right = len(row)
        while left < right:
            mid = (left + right) // 2
            if row[mid] < 0:
                right = mid
            else:
                left = mid + 1
        return len(row) - left
    total_negatives = 0
    for row in grid:
        total_negatives += countNegativesInRow(row)
    return total_negatives


grid = [[4, 3, 2, 1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
print(countNegatives(grid))