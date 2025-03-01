def merge_two_sorted_lists(list1, list2):
    # Initialize pointers for both lists
    i, j = 0, 0
    result = []  # Initialize an empty list to store the merged result

    # Traverse both lists and merge them in sorted order
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])  # Add the smaller element to the result list
            i += 1
        else:
            result.append(list2[j])  # Add the smaller element to the result list
            j += 1

    # If there are remaining elements in list1, add them to the result
    while i < len(list1):
        result.append(list1[i])
        i += 1

    # If there are remaining elements in list2, add them to the result
    while j < len(list2):
        result.append(list2[j])
        j += 1

    return result  # Return the merged sorted list

list1 = [1, 3, 5]
list2 = [2, 4, 6]
print(merge_two_sorted_lists(list1, list2))