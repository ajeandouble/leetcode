# Notes Dynamic Programming

## Basics

> A dynamic programming problem is characterized by two main features: **_optimal substructure_** and **_overlapping subproblems_**.

### Optimal Substructure

> In the context of dynamic programming, a problem exhibits optimal substructure if an optimal solution to the problem can be constructed from optimal solutions to its subproblems. This means that if you solve the subproblems optimally, you can piece them together to create an optimal solution for the larger problem.
> an always generating new subproblems.

[Overlapping Subproblems @wikipedia](https://en.wikipedia.org/wiki/Optimal_substructure)

### Overlapping Subproblems

> A problem is said to have overlapping subproblems if the problem can be broken down into subproblems which are reused several times or a recursive algorithm for the problem solves the same subproblem over and over rather than always generating new subproblems.

[Overlapping Subproblems @wikipedia](https://en.wikipedia.org/wiki/Overlapping_subproblem)

> For example, the problem of computing the Fibonacci sequence exhibits overlapping subproblems. The problem of computing the nth Fibonacci number F(n), can be broken down into the subproblems of computing F(n − 1) and F(n − 2), and then adding the two. The subproblem of computing F(n − 1) can itself be broken down into a subproblem that involves computing F(n − 2). Therefore, the computation of F(n − 2) is reused, and the Fibonacci sequence thus exhibits overlapping subproblems.an always generating new subproblems.

[Overlapping Subproblems @wikipedia](https://en.wikipedia.org/wiki/Overlapping_subproblem)

Dynamic programming techniques improve algorithm complexity by re-using pre-computed subproblems answers.

### Linear Sequence

Your input is 1D array/list! Duh!

### Linear Time

`O(N)` !

### Constant transition

The state at position `i` depends only on a fixed number at earlier or later positions. That is too say you don't loop over on a variable number of subproblems to solve the current subproblem.

Hence it's solvable in `O(N)` time.

## Techniques

### Tabulation vs Memoization

Tabulation is **_bottom up_**.
Memoization is **_top down_**.

> Tabulation and memoization are two main techniques in dynamic programming, both addressing overlapping subproblems. Tabulation uses a bottom-up approach, iteratively building a table of solutions to subproblems. Memoization, on the other hand, uses a top-down approach with recursion, storing results of function calls (subproblems) in a lookup table

### Caching

`@cache` or `@lru_cache` can be used in _python_ to do memoization instead of keeping a dictionary updated.

### Which Direction?

You can technically but doesn't feel natural to implement **_backward DP_** solutions using recursivity.
Hence for tabulation you would either go forward or backward:

```
Q: Can I decide what to do now based only on the past?
→ YES: forward

Q: Do I need to know what will happen in the future to decide now?
→ YES: backward

Q: Are the decisions “cooling down” or “jumping forward”?
→ YES: backward

Q: Am I building something cumulatively, like max score or max sum so far?
→ YES: forward
```

#### Examples

_House Robber Either_ Can go both ways, but often left→right feels natural `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`
_Brainpower_ Backward Need to look ahead (skip questions) `dp[i] = max(dp[i+1], gain + dp[i+skip])`

#### Thinking backward

Recognizing When to Use the "Last Action" Perspective:

1. Look for Dependency Patterns
   When the result of an action changes the environment for future actions, consider whether thinking backwards might simplify things:

In Burst Balloons, bursting a balloon changes which balloons become adjacent, affecting future points
When bursting balloon k, the points you get depend on which balloons are left, which depends on the order of previous bursts

2. Notice State Definition Difficulties
   If you're struggling to define a forward-moving state:

If defining DP[i][j] as "best result starting from first action" leads to complex state transitions
If you find yourself needing to track too many changing variables

3. Problem Exhibits "Non-Overlapping Subproblems" When Going Forward

When a forward approach keeps leading to subproblems that can't be cleanly separated
When actions create dependencies between seemingly separate parts of the problem

4. When Greedy Approaches Fail

You've tried greedy approaches (like "burst highest value first") and found counterexamples

## DP problems classified

### Linear Sequence DP

These are **_linear sequence_**, **_linear time_**, **_constant transition_** problems.

This covers:

- House Robber
- Climbing Stairs
- Brainpower (in reverse)
- Max Sum of Non-Adjacent Elements
- Fibonacci variations

This **does NOT** cover:

- Knapsack (why? because `dp[i][w]` depends on looping over many choices of weights/costs)
- Longest Increasing Subsequence with O(n^2) (dp[i] = max(dp[j] + 1) for all j < i and arr[j] < arr[i])

### TODO...
