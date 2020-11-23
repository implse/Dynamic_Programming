# Given a rod of length n and an array of prices that contains prices of all pieces of size smaller than n.
# Determine how to cut the rod in order to maximize the profit.


# Time Complexity : O(n^2) / Space Complexity : O(n*p)
def rodCutting(rod_length, prices):
    ln = len(prices)
    dp_table = [[0] * (rod_length + 1) for x in range(ln)]

    for i in range(1, ln):
        for j in range(1, rod_length + 1):
            if i <= j:
                dp_table[i][j] = max(dp_table[i - 1][j], prices[i] + dp_table[i][j - i])
            else:
                dp_table[i][j] = dp_table[i - 1][j]

    max_profit = dp_table[ln - 1][rod_length]
    col_idx = rod_length
    row_idx = ln - 1

    while col_idx > 0 or row_idx > 0:
        if dp_table[row_idx][col_idx] == dp_table[row_idx - 1][col_idx]:
            row_idx = row_idx - 1
        else:
            print("We make a cut at :", row_idx, "mêtre")
            col_idx = col_idx - row_idx
    return max_profit
# Test
rod_length = 5
prices = [0, 2, 5, 7, 3]

print(rodCutting(rod_length, prices))
