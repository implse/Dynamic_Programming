# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint stopping
# you from robbing each of them is that adjacent houses have security system connected
# and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.

# Dynamic Programming
def houseRobber(values):
    if len(values) == 0:
        return 0
    if len(values) == 1:
        return values[0]
    if len(values) == 2:
        return max(values[0], values[1])
    else:
        dp = [0 for _ in range(len(values))]
        dp[0] = values[0]
        dp[1] = max(values[0], values[1])

        for i in range(2, len(values)):
            dp[i] = max(dp[i - 2] + values[i], dp[i - 1])
    return dp[-1]

# Test
values = [2, 7, 9, 3, 1] # 12
print(houseRobber(values))


# Brute Force: Time O(2^n) / Space O(n)
def houseRobber(values):
    def houseRobberHelper(index):
        if index >= len(values):
            return 0
        else:
            return max(values[index] + houseRobberHelper(index + 2), houseRobberHelper(index + 1))
    return houseRobberHelper(0)

values = [2, 7, 9, 3, 1] # 12
print(houseRobber(values))
