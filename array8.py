def minimumScore(nums, k):
    min_num = min(nums)
    max_num = max(nums)

    if min_num == max_num:
        return 0

    min_score = max_num - min_num

    for num in nums:
        potential_min = num - k
        potential_max = num + k
        min_num = min(min_num, potential_min)
        max_num = max(max_num, potential_max)
        min_score = min(min_score, max_num - min_num)

    return min_score
nums = [1]
k = 0

print(minimumScore(nums, k))
