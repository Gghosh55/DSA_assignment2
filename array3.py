def findLHS(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    max_length = 0
    for num in freq.keys():
        if num + 1 in freq:
            length = freq[num] + freq[num + 1]
            max_length = max(max_length, length)

    return max_length
nums = [1, 3, 2, 2, 5, 2, 3, 7]

print(findLHS(nums))
