# Recursive fibonacci - use call stack - Time complexity : O(2^n)
def fib_recursive(n):
  if n <= 1:
    return n
  return fib_recursive(n-1)+ fib_recursive(n-2)


# Memoize Recursive fibonacci - Time complexity O(n) - Space complexity O(n)
def fib_memoize(n, cache = {}):
    if n <= 1:
        return n
    elif n not in cache:
        cache[n] =  fib_memoize(n-1) + fib_memoize(n-2)
    return cache[n]


# Bottom Up fibonacci - Time complexity O(n) - Space complexity O(1)
def fibo_bottomUp(n):
  if n <= 1:
    return n
  f_minus_two = 0
  f_minus_one = 1
  for _ in range(1, n):
    result = f_minus_two + f_minus_one
    f_minus_two, f_minus_one = f_minus_one, result
  return f_minus_one
