# https://codereview.stackexchange.com/questions/20569/dynamic-programming-knapsack-solution

# Solve the knapsack problem by finding the most valuable subsequence
# of items that weighs no more than maxweight.
#
# items must be a sequence of pairs (value, weight), where value is a
# number and weight is a non-negative integer.
#
# maxweight is a non-negative integer.
#
# Return a pair whose first element is the sum of values in the most
# valuable subsequence, and whose second element is the subsequence.

# DP : Bottom up Solution
def knapsack(items, maxweight):
    bestvalues = [[0] * (maxweight + 1) for _ in range(len(items) + 1)]
    for i, (value, weight) in enumerate(items):
        i += 1
        for capacity in range(maxweight + 1):
            if weight > capacity:
                bestvalues[i][capacity] = bestvalues[i - 1][capacity]
            else:
                candidate1 = bestvalues[i - 1][capacity]
                candidate2 = bestvalues[i - 1][capacity - weight] + value
                bestvalues[i][capacity] = max(candidate1, candidate2)

    items_select = reconstruction(bestvalues, len(items), maxweight)

    return bestvalues[len(items)][maxweight], items_select

def reconstruction(bestvalues, i, j):
    reconstruction = []
    for i in reversed(range(1, i + 1)):
        if bestvalues[i][j] != bestvalues[i - 1][j]:
            reconstruction.append(items[i - 1])
            j -= items[i - 1][1]
    reconstruction.reverse()
    return reconstruction

# Test

# max weight
weight = 7
# (values, weight) pairs
items = [(1,1), (4, 3), (5, 4), (7, 5)]

print(knapsack(items, weight))
