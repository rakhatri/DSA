def move_zeroes(nums):
    """
    Function to move all 0's to the end of the array while maintaining the order of non-zero elements.
    :param nums: List[int] -> A list of integers
    :return: None -> The list is modified in place
    """
    non_zero_index = 0  # Pointer to track the position of the next non-zero element

    # Move non-zero elements to the front of the list
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index] = nums[i]
            non_zero_index += 1

    # Fill the remaining positions with zeros
    while non_zero_index < len(nums):
        nums[non_zero_index] = 0
        non_zero_index += 1

nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
move_zeroes(nums)
print(nums)