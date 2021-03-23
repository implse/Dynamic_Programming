# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,

# Recursive fibonacci - use call stack - Time Complexity : O(2^n)
calculation = 0
def fibonacci_recursive(n):
    global calculation
    calculation += 1
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


# Top-Down Memoize Recursive fibonacci - Time Complexity O(n) - Space Complexity O(n)
def fibonacci_memoize(n, cache = {}):
    if n <= 1:
        return n
    elif n not in cache:
        cache[n] =  fibonacci_memoize(n - 1) + fibonacci_memoize(n - 2)
    return cache[n]


# Bottom-Up Iterative fibonacci - Time Complexity O(n) - Space Complexity O(1)
def fibonacci_bottom_up(n):
  if n <= 1:
    return n
  f_minus_two = 0
  f_minus_one = 1
  for _ in range(1, n):
    result = f_minus_two + f_minus_one
    f_minus_two, f_minus_one = f_minus_one, result
  return f_minus_one

# Bottom-Up Iterative fibonacci - Time Complexity O(n) - Space Complexity O(n)
def fibonacci_bottom_up(n):
    if n < 2:
        return n
    cache = [0, 1]
    for i in range(2, n + 1):
        cache.append(cache[i - 1] + cache[i - 2])
    return cache[n]
