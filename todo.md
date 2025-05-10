# TODO

## Resources

[Geohot - Hackerrank warmup @youtube](https://www.youtube.com/watch?v=Q8nhQSp__3s)
[Tushar Roy - Coding Made Simple @youtube](https://www.youtube.com/@tusharroy2525)
[WilliamFiset's youtube @youtube](https://www.youtube.com/@WilliamFiset-videos)

### DP

[Negamax - Chess Programming Wikip](<https://www.chessprogramming.org/Negamax#:~:text=a%20common%20way%20of%20implementing,min(%2Da%2C%20%2Db)>)

## The Ultimate Dynamic Programming Roadmap

[The Ultimate Dynamic Programming Roadmap](https://www.reddit.com/r/leetcode/comments/14o10jd/the_ultimate_dynamic_programming_roadmap/)

## Group 1 (Warmup)

Basic questions to get a feel of DP.

- [x] [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) - Linear time solution
- [x] [N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/) - Linear time solution
- [x] [Perfect Squares](https://leetcode.com/problems/perfect-squares/) (maybe)

## Group 2 (Linear Sequence, Linear Time, Constant Transition)

DP solution requires us to solve the sub problem on every prefix of the array. A prefix of the array is a subarray from `0` to `i` for some `i`.

- [x] [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) - Linear time solution
- [x] [Minimum Time to Make Rope Colorful](https://leetcode.com/problems/minimum-time-to-make-rope-colorful/)
- [x] [House Robber](https://leetcode.com/problems/house-robber/)
- [x] [Decode Ways](https://leetcode.com/problems/decode-ways/)
- [x] [Minimum Cost for Tickets](https://leetcode.com/problems/minimum-cost-for-tickets/)
- [x] [Solving Questions with Brainpower](https://leetcode.com/problems/solving-questions-with-brainpower/)

## Group 3 (On Grids)

DP table will have the same dimensions as grid, the state at cell `i,j` will be related to the grid at cell `i,j`.

- [x] [Unique Paths](https://leetcode.com/problems/unique-paths/)
- [x] [Unique Paths II](https://leetcode.com/problems/unique-paths-ii/)
- [x] [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)
- [x] [Count Square Submatrices with All Ones](https://leetcode.com/problems/count-square-submatrices-with-all-ones/)
- [x] [Maximal Square](https://leetcode.com/problems/maximal-square/)
- [x] [Dungeon Game](https://leetcode.com/problems/dungeon-game/)

## Group 4 (Two Sequences, O(NM) Style)

`DP[i][j]` is some value related to the problem solved on prefix of sequence `1` with length `i`, and prefix on sequence `2` with length `j`.

- [x] [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
- [x] [Uncrossed Lines](https://leetcode.com/problems/uncrossed-lines/) (longest common subsequence)
- [x] [Minimum ASCII Delete Sum for Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/)
- [x] [Edit Distance](https://leetcode.com/problems/edit-distance/)
- [x] [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/)
- [ ] [Shortest Common Supersequence](https://leetcode.com/problems/shortest-common-supersequence/)

## Group 5 (Interval DP)

DP problem is solved on every single interval (subarray) of the array

- [x] [Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/)
- [x] [Stone Game VII](https://leetcode.com/problems/stone-game-vii/)
- [ ] [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)
- [ ] [Minimum Cost Tree from Leaf Values](https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/) (hard to see interval)
- [ ] [Strange Printer](https://leetcode.com/problems/strange-printer/) (hard)
- [ ] [Burst Balloons](https://leetcode.com/problems/burst-balloons/) (hard)

## Group 6 (Linear Sequence Transition like N² Longest Increasing Subsequence)

DP problem is solved on every prefix of the array. Transition is from every index `j < i`.

- [ ] [Count Number of Teams](https://leetcode.com/problems/count-number-of-teams/)
- [ ] [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
- [ ] [Partition Array for Maximum Sum](https://leetcode.com/problems/partition-array-for-maximum-sum/)
- [ ] [Largest Sum of Averages](https://leetcode.com/problems/largest-sum-of-averages/)
- [ ] [Filling Bookcase Shelves](https://leetcode.com/problems/filling-bookcase-shelves/)

## Group 7 (Knapsack-like)

DP state is similar to the classical knapsack problem.

- [ ] [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)
- [ ] [Number of Dice Rolls with Target Sum](https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/)
- [ ] [Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/)
- [ ] [Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes/)
- [ ] [Coin Change](https://leetcode.com/problems/coin-change/)
- [ ] [Coin Change II](https://leetcode.com/problems/coin-change-ii/)
- [ ] [Target Sum](https://leetcode.com/problems/target-sum/)
- [ ] [Last Stone Weight II](https://leetcode.com/problems/last-stone-weight-ii/)
- [ ] [Profitable Schemes](https://leetcode.com/problems/profitable-schemes/) (hard)

## Group 8 (Topological Sort with Graphs - Advanced, Optional)

Solve DP on all subgraphs that are connected to each node

- [ ] [Longest String Chain](https://leetcode.com/problems/longest-string-chain/)
- [ ] [Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)
- [ ] [Course Schedule III](https://leetcode.com/problems/course-schedule-iii/)

## Group 9 (DP on Trees - Advanced, Optional)

Solve DP problem on all subtrees.

- [ ] [House Robber III](https://leetcode.com/problems/house-robber-iii/)
- [ ] [Binary Tree Cameras](https://leetcode.com/problems/binary-tree-cameras/)

## Project Euler

`Yes!`
