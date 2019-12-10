# Given a matrix of size N * M  and a list of block cells, find the numbers of possible ways to reach the bottom right cell in a matrix starting from (0, 0)

# going down and going left are the only possible way to go.


# [0, 0, 0, 1]
# [0, 1, 0, 0],
# [0, 0, 0, 1],
# [1, 0, 0, 0]

m = 4
n = 4
block_cells = [(0, 3), (1, 1), (2, 3), (3, 0)]

def totalWays(n, m, block):
    grid = [[0 for _ in range(n)] for _ in range(m)]

    for r in range(len(grid)):
        if (r, 0) not in block_cells:
            grid[r][0] = 1
    for c in range(len(grid[0])):
        if (0, c) not in block_cells:
            grid[0][c] = 1

    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            if (i, j) not in block_cells:
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
    return grid[-1][-1]

print(totalWays(n, m, block_cells))
