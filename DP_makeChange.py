# Given an integer representing a specific amount of change and a set of coin sizes,
# determine the minimum number of coins required to make that amount of change.
# You may assume there is always a 1 cent coin.

# coins = (1, 5, 10, 25)
# change(1) = 1 (1)
# change(6) = 2 (5 + 1)
# change(47) = 5 (25 + 10 + 10 + 1 + 1)

# Brute Force Approach:
# Recursively try every possible combination to find the smallest.
# Each recursive step, we will try each coin possibility that is less than the remaining total.
# Substract the coin value from the total remaining until the remaining coin value is 0.

# Brute Force Recursive
def makeChange(amount, coins):
  if amount == 0:
    return 0
  minCoins = float("inf")
  for coin in coins:
    if amount - coin >= 0:
      currMin = makeChange(amount - coin, coins)
      minCoins = min(currMin, minCoins)
  return minCoins + 1

# DP Memoize Top-Down
def makeChange(amount, coins):
  memo = [0 for _ in range(amount + 1)]
  return makeChange_helper(amount, coins, memo)

def makeChange_helper(amount, coins, memo):
    if memo[amount] == 0:
      if amount == 0:
        return 0
      minCoins = float("inf")
      for coin in coins:
        if amount - coin >= 0:
          currMin = makeChange(amount - coin, coins)
          minCoins = min(currMin, minCoins)
      memo[amount] = minCoins + 1
    return memo[amount]

# DP Memoize Bottom-Up
def makeChange(amount, coins):
  memo = [0 for _ in range(amount + 1)]
  for i in range(1, amount + 1):
      minCoins = float("inf")
      for coin in coins:
        if i - coin >= 0:
          minCoins = min(minCoins, memo[i - coin])
      memo[i] = minCoins + 1
  return memo[amount]

# Test
coins = [1, 5, 10, 25]
print(makeChange(47, coins))

coins = [10, 6, 1]
print(makeChange(12, coins))
