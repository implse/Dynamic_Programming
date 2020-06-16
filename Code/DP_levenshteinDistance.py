# Write a function that takes in two strings and returns the minimum number of edit
# operations that need to be performed on the first string to obtain the second string.
#
# There are three edit operations: insertion of a character, deletion of a character,
# and substitution of a character for another.

# Time O(N*M) == O(len(str1)*len(str2)) / Space O(N*M)
def levenshteinDistance(str1, str2):
	# Matrix fill with 0
	matrix = [[0 for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]
	# Base case row
	matrix[0] = [c for c in range(len(str1) + 1)]
	# Base case col
	for r in range(1, len(str2) + 1):
		matrix[r][0] = r
	# Apply formula
	for i in range(1, len(str2) + 1):
		for j in range(1, len(str1) + 1):
			if str2[i - 1] == str1[j - 1]:
				matrix[i][j] = matrix[i - 1][j - 1]
			else:
				matrix[i][j] = 1 + min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1])
	return matrix[-1][-1]
