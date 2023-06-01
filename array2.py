def distributeCandies(candyType):
    distinct_candies = set(candyType)  # Step 1
    max_candies = min(len(distinct_candies), len(candyType) // 2)  # Step 2
    return max_candies  # Step 3
candyType = [1, 1, 2, 2, 3, 3]

print(distributeCandies(candyType))
