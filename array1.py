def arrayPairSum(nums):
    nums.sort()  # Step 1
    max_sum = 0  # Step 2

    for i in range(0, len(nums), 2):  # Step 3
        max_sum += nums[i]  # Step 4

    return max_sum  # Step 6
nums = [1, 4, 3, 2]

print(arrayPairSum(nums))
