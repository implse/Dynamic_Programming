# Recursive factorial
def fact_recursive(n):
  if n == 1:
    return n
  return n * fact_recursive(n - 1)


# Memoize factorial
def fact_memoize(n, cache = {}):
  if n == 1:
    return n
  elif n not in cache:
    cache[n] = n * fact_memoize(n - 1)
  return cache[n]


# Bottom Up factorial
def fact_bottomUp(n):
  result = 1
  for i in range(1, n+1):
    result *= i
  return result
