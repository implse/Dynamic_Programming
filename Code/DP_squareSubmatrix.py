# Given a 2D boolean array, fincd the largest sqaure subarray of true values.
# You should return the side length of the largest sqaure subarray.


def squareMatrix(arr):
    maxSquare = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            maxSquare = max(maxSquare, squareMatrixRecursive(arr, i, j) )
    return maxSquare

def squareMatrixRecursive(arr, i, j):
    if i == len(arr) or j == len(arr[0]):
        return 0
    if arr[i][j] == False:
        return 0
    return 1 + min(squareMatrixRecursive(arr, i+1, j), squareMatrixRecursive(arr, i, j+1), squareMatrixRecursive(arr, i+1, j+1))

# Test
sq = [
[True, True, True, True],
[False, True, True, False]
 ]

print(squareMatrix(sq))
