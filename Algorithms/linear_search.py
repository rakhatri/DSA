def linear_search(list, target):
    """
    Returns the index position if found else returns None
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print(f"Target found at Index: {index}")
    else:
        print("Target not found in list")


numbers = [i for i in range(1, 10)]
result = linear_search(numbers, 12)
print(result)
verify(result)

result = linear_search(numbers, 6)
print(result)
verify(result)
