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

#### Bottom Up Approach (Iteration)

Going Bottom Up is a way to avoid recursion, saving the memory cost that recursion incurs when it builds up the call stack.

Put simply, a bottom-up algorithm "starts from the beginning," while a recursive algorithm often "starts from the end and works backwards."

Start with the smallest solutions, the smallest subproblems and the build up each solution until we arrive at the solution to the larger subproblem.

A benefit to the bottom up approach is that we can save space since we are working our way up. We only need to really memoize the last 2 values, which means we can achieve constant space O(1).

#### Top Down Approach (Recursion)

Top Down approach start from the top (the desired
result) and recursively break the solution into smaller pieces that you compute individually and
piece back together.

As you solve the problem recursively, you memoize the results of each subproblem so that you never have to recompute them.

This is often the easier solution to understand because it is only a small step from a basic recursive solution to a top down
solution.

### Solving Problem Using DP

We can solve a problem using DP if it has:

- Optimal Substructure.

- Overlapping subproblems.

then find Brute force solution. (draw recursive Tree)

#### Common patterns to identify Dynamic Programming problems

- Maximization

- Minimization

- Optimization

- Counting

### Dynamic Programming vs Greedy Algorithms

A lot of confusion between the two, even some overlap.

Greedy algorithms consider only local optimizations.

Dynamic programming consider every option and solve the all sub problems and then select one that would lead to an optimal solution.


### F.A.S.T Strategy

Generalized approach to solving any dynamic programming problem.

Takes brute force solution and optimizes it.

Four steps in the FAST method:

1 - Find solution.

2 - Analyze the first solution.(Brute Force)

3 - Identify the Subproblems.

4 - Turn the solution around.


#### Analyze the brute force solutions

Estimate Time Complexity based on the number of recursive calls.

Time Complexity is O(2^n) 

Space Complexity is O(n)
