def insertion_sort(nums):
    n = len(nums)
    for current in range(1, n):
        currentCard = nums[current]
        currentPosition = current-1

        while currentPosition >= 0:
            if nums[currentPosition] < currentCard:
                break
            else:
                nums[currentPosition + 1] = nums[currentPosition]
                currentPosition -= 1
        nums[currentPosition + 1] = currentCard
    return nums

nums = [12, 25, 11, 34, 90, 22]
print(nums)
print(insertion_sort(nums))