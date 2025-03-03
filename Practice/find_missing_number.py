def find_missing_number(nums):
    """
    Function to find the missing number in the array.
    :param nums: List[int] -> A list of distinct integers in the range [0, n]
    :return: int -> The missing number in the range
    """
    max_num = 0
    # O(n*n)
    for num in nums:
        if num > max_num:
            max_num = num
    print(max_num)
    dummy_list = [elem for elem in range(0, max_num+1)]
    if len(dummy_list) == len(nums):
        dummy_list.append(max_num + 1)
    print(dummy_list)
    for num in dummy_list:
        if num not in nums:
            return num



print(find_missing_number([0,1]))
