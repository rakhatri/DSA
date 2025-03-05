def searchRange(nums, target):
    """
    Find the starting and ending position of a given target value in a sorted array.
    Use binary search to find both the first and last occurrence of the target.
    """

    def findFirst(nums, target):
        """
        Find the first occurrence of the target using binary search.
        """
        left, right = 0, len(nums) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result

    def findLast(nums, target):
        """
        Find the last occurrence of the target using binary search.
        """
        left, right = 0, len(nums) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result

    start = findFirst(nums, target)
    end = findLast(nums, target)

    return [start, end]
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(searchRange(nums, target))