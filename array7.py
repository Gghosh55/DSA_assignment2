def isMonotonic(nums):
    isIncreasing = True
    isDecreasing = True

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            isDecreasing = False
        if nums[i] < nums[i - 1]:
            isIncreasing = False

    return isIncreasing or isDecreasing
nums = [1,2,2,3]

print(isMonotonic(nums))
