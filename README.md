# Dynamic Programming


> THOSE WHO CANNOT REMEMER THE PAST ARE CONDEMNED TO REPEAT IT.
>
> Dynamic Programming


Dynamic programming is a method for solving problems by breaking them down into a collection of simple subproblems, solving each of those subproblems just once, and storing their solutions. This saves computation time.

__Dynamic Programming -> Dynamic Optimization.__

__Dynamic Programming -> Recursion + Memoization.__

#### 7 Steps to solve a Dynamic Programming problem :

  1 - Recognize a DP problem.

  2 - Identify problem variables.

  3 - Clearly express the recurrence relation.

  4 - Identify the base cases.

  5 - Decide if you want to implement it iteratively or recursively.

  6 - Add memoization.

  7 - Determine time complexity.

  __Recursion:__ solve sub problems recursively.

  __Memoization:__ store already computed values in cache. (Memoization means caching)

### Memoization

Memoization is a technique that is closely associated with Dynamic Programming.
It is used for storing the results of expensive function calls and returning the cache result when the same inputs occur again.

## Technique

#### Bottom Up Approach

Going bottom-up is a way to avoid recursion, saving the memory cost that recursion incurs when it builds up the call stack.

Put simply, a bottom-up algorithm "starts from the beginning," while a recursive algorithm often "starts from the end and works backwards."
