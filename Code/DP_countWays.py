# A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
# Implement a method to count how many possible ways the child can run up the stairs.

# Brute Force - Time Complexity : O(n^2)
def countWays(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return countWays(n-1) + countWays(n-2) + countWays(n-3)

# Memoize Top Down - Time complexity O(n)
def countWays(n, memo = {}):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = countWays(n-1, memo) + countWays(n-2, memo) + countWays(n-3, memo)
    return memo[n]

# Memoize Bottum Up - Time complexity O(n)
def countWays(n) :
    memo = dict()
    memo[0] = 1
    memo[1] = 1
    memo[2] = 2
    for i in range(3, n + 1) :
        memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
    return memo[n]
