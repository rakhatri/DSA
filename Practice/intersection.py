def intersection(nums1, nums2):
    """
    Function to find the intersection of two integer arrays.
    :param nums1: List[int] -> First array of integers
    :param nums2: List[int] -> Second array of integers
    :return: List[int] -> An array of unique integers present in both arrays
    """
    nums_set1 = set(nums1)
    intersection_set = set()
    for elem in nums2:
        if elem in nums_set1:
            intersection_set.add(elem)
    return list(intersection_set)


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersection(nums1, nums2))


