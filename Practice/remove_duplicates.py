def remove_duplicates(lst):
    # Your code goes here
    unique_list = []
    for elem in lst:
        if elem not in unique_list:
            unique_list.append(elem)
            print(unique_list)
    return unique_list


print(remove_duplicates([1,2,2,3,3,4,4,5,5]))