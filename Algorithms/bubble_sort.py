def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums




nums = [12, 25, 11, 34, 90, 22]
print(bubble_sort(nums))