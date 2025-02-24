def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = list[midpoint] - 1
    return None


def verify(index):
    if index is not None:
        print(f"Target found at Index: {index}")
    else:
        print("Target not found in list")


numbers = [i for i in range(1, 10)]
result = binary_search(numbers, 12)
print(result)
verify(result)

result = binary_search(numbers, 6)
print(result)
verify(result)
