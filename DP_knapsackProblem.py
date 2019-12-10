# https://codereview.stackexchange.com/questions/20569/dynamic-programming-knapsack-solution


def knapsack(items, maxweight):
    bestvalues = [[0] * (maxweight + 1) for i in range(len(items) + 1)]
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
    while i > 0:
        if bestvalues[i][j] != bestvalues[i - 1][j]:
            reconstruction.append(items[i - 1])
            j -= items[i - 1][1]
        i -= 1
    reconstruction.reverse()
    return reconstruction

# Test

# max weight
weight = 7
# (values, weight) pairs
items = [(1,1), (4, 3), (5, 4), (7, 5)]

print(knapsack(items, weight))
