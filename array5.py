def maximumProduct(nums):
    nums.sort()

    max_product = nums[-1] * nums[-2] * nums[-3]

    if nums[0] < 0 and nums[1] < 0:
        max_product = max(max_product, nums[0] * nums[1] * nums[-1])

    return max_product
nums = [1, 2, 3]

print(maximumProduct(nums))
