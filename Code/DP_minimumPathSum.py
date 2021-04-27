# Given an m * n grid filled with non negative numbers, find a path from topleft to
# bottom right which minimize the sum of the numbers along its path.

grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]


# Dynamic Programming Solution
from copy import deepcopy

def minimum_path_sum(grid):

    dp = deepcopy(grid)

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if row == 0 and col == 0:
                dp[row][col] = grid[row][col]
            elif row == 0 and col > 0:
                dp[row][col] = dp[row][col - 1] + grid[row][col]
            elif row > 0 and col == 0:
                dp[row][col] = dp[row - 1][col] + grid[row][col]
            else:
                dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + grid[row][col]
    return dp[-1][-1]

print(minimum_path_sum(grid))
