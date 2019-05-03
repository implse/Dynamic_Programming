# Given a square matrix the size N find the numbers of possible ways to reach a cell in a matrix starting from (0, 0)
# going down and going left are the only possible way to go.

def totalWays(n, end_position):
    # Grid
    grid = [[0 for c in range(n)] for r in range(n)]
    # Initialize grid base case : first row all 1 first col all 1
    grid[0] = [1 for _ in range(len(grid[0]))]
    for r in grid:
        r[0] = 1

    for r in range(1, len(grid[0])):
        for c in range(1, len(grid)):
            grid[r][c] = grid[r-1][c] + grid[r][c-1]
    print(grid)
    return grid[end_position[0]][end_position[1]]

print(totalWays(5, (4, 4)))
