def recursive_binary_search(list, target):
    if len(list) == 0:
        # Base Case
        return False
    else:
        # Base Case
        midpoint = (len(list)) // 2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint + 1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)


def verify(result):
    print(f"Target found: {result}")


numbers = [i for i in range(1, 10)]
result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 6)
verify(result)
