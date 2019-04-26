# Given an integer representing a specific amount of change and a set of coin sizes,
# determine the minimum number of coins required to make that amount of change.
# You may assume there is always a 1 cent coin.

# coins = (1, 5, 10, 25)
# change(1) = 1 (1)
# change(6) = 2 (5 + 1)
# change(47) = 5 (25 + 10 + 10 + 1 + 1)

# Brute Force:

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



# Test
coins = [1, 5, 10, 25]
print(makeChange(47, coins))

coins = [10, 6, 1]
print(makeChange(12, coins))
