# Given a n m * n martix filled with 0 and 1, find the largest square containing only 1
# and return its area.

m = [
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]
]

def maximal_sqaure(m):
    height = len(m)
    width = len(m[0])
    dp = [[0] * width] * height
    answer = 0

    for row in range(height):
        for col in range(width):
            if m[row][col] == 1:
                dp[row][col] = 1
                if row > 0 and col > 0:
                    dp[row][col] += min(dp[row - 1][col], dp[row][col - 1], dp[row - 1][col - 1])
                    answer = max(answer, dp[row][col])
    return answer ** 2


print(maximal_sqaure(m))
