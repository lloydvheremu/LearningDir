# 40-Day LeetCode Tier 1 Sprint

**Start Date:** Day 1 (fill in your start date)
**Commitment:** 1 hour/day | ~2 problems/day
**Language:** Python
**Goal:** Master all 10 Tier 1 interview patterns

---

## How to Use This Plan

- Solve both problems before checking any solution.
- After solving, look up the optimal approach and compare it to yours.
- If you're stuck for more than 20 minutes, look at a hint only — not the full solution.
- Mark each problem as you complete it: `[ ]` → `[x]`
- Difficulty labels: 🟢 Easy | 🟡 Medium | 🔴 Hard

---

## Pattern 1: Hash Maps
**Days 1–4 | ~8 Problems**

**Core idea:** Trade space for time. Store what you've already seen in a dict so you can answer lookups in O(1) instead of re-scanning the array.

**When to recognize it:** You're counting frequencies, detecting duplicates, matching pairs, or need to check "have I seen this before?"

**Python toolkit:**
```python
freq = {}
freq[x] = freq.get(x, 0) + 1

from collections import defaultdict, Counter
Counter(nums).most_common(k)
```

---

### Day 1
- [x] 🟢 [#1 Two Sum](https://leetcode.com/problems/two-sum/) — Classic complement lookup *(already solved on your profile)*
  - **Alt:** [ ] 🟢 [#1512 Number of Good Pairs](https://leetcode.com/problems/number-of-good-pairs/) — Same hash-map counting idea, unsolved
- [x] 🟢 [#217 Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) — Seen-set detection *(already solved on your profile)*
  - **Alt:** [ ] 🟡 [#219 Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/) — Same seen-set idea, adds an index-distance twist, unsolved

### Day 2
- [x] 🟢 [#242 Valid Anagram](https://leetcode.com/problems/valid-anagram/) — Character frequency match *(already solved on your profile)*
  - **Alt:** [ ] 🟡 [#1347 Minimum Number of Steps to Make Two Strings Anagram](https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/) — Same frequency-match idea, unsolved
- [ ] 🟡 [#49 Group Anagrams](https://leetcode.com/problems/group-anagrams/) — Sorted key grouping

### Day 3
- [ ] 🟢 [#383 Ransom Note](https://leetcode.com/problems/ransom-note/) — Character availability check
- [ ] 🟡 [#347 Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) — Counter + bucket sort

### Day 4
- [ ] 🟡 [#128 Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) — Set membership, O(n) chain detection
- [ ] 🟡 [#560 Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) — Prefix sum + hash map

---

## Pattern 2: Two Pointers
**Days 5–8 | ~8 Problems**

**Core idea:** Use two indices moving through an array (often sorted) to avoid nested loops. Instead of O(n²) comparisons, you converge inward or move together.

**When to recognize it:** Sorted array, pair/triplet sums, palindrome check, partition in-place, remove duplicates.

**Python toolkit:**
```python
left, right = 0, len(nums) - 1
while left < right:
    if condition:
        left += 1
    else:
        right -= 1
```

---

### Day 5
- [ ] 🟢 [#125 Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) — Converging pointers with skip logic
- [x] 🟡 [#167 Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) — Sorted array inward squeeze *(already solved on your profile)*
  - **Alt:** [ ] 🟡 [#633 Sum of Square Numbers](https://leetcode.com/problems/sum-of-square-numbers/) — Same sorted inward-squeeze idea, unsolved

### Day 6
- [x] 🟡 [#15 3Sum](https://leetcode.com/problems/3sum/) — Fix one, two-pointer the rest *(already solved on your profile)*
  - **Alt:** [ ] 🟡 [#18 4Sum](https://leetcode.com/problems/4sum/) — Direct extension of 3Sum, unsolved
- [ ] 🟢 [#26 Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) — Slow/fast write pointer

### Day 7
- [ ] 🟡 [#11 Container With Most Water](https://leetcode.com/problems/container-with-most-water/) — Greedy pointer move
- [x] 🟢 [#344 Reverse String](https://leetcode.com/problems/reverse-string/) — In-place swap *(already solved on your profile)*
  - **Alt:** [ ] 🟢 [#283 Move Zeroes](https://leetcode.com/problems/move-zeroes/) — Same in-place two-pointer swap idea, unsolved

### Day 8
- [ ] 🟡 [#75 Sort Colors](https://leetcode.com/problems/sort-colors/) — Dutch National Flag, three-pointer
- [ ] 🟡 [#16 3Sum Closest](https://leetcode.com/problems/3sum-closest/) — Two pointer variation

---

## Pattern 3: Sliding Window
**Days 9–12 | ~8 Problems**

**Core idea:** Maintain a window of elements using two pointers (left/right). Expand right to grow, shrink left when a constraint is violated. Avoids recalculating the window from scratch each step.

**When to recognize it:** "Longest/shortest subarray or substring where [condition]." Any contiguous subsequence problem.

**Python toolkit:**
```python
left = 0
window = {}
for right in range(len(s)):
    # add s[right] to window
    while window_is_invalid:
        # remove s[left] from window
        left += 1
    # update answer
```

---

### Day 9
- [ ] 🟢 [#121 Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) — Min-so-far + max-profit
- [ ] 🟡 [#3 Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) — Classic variable window

### Day 10
- [ ] 🟡 [#424 Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) — Max freq trick
- [ ] 🟡 [#567 Permutation in String](https://leetcode.com/problems/permutation-in-string/) — Fixed-size window, frequency match

### Day 11
- [ ] 🔴 [#76 Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) — Variable window, shrink for minimum
- [ ] 🟡 [#209 Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) — Shrink when constraint met

### Day 12
- [ ] 🟡 [#1004 Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) — Window with k-flip budget
- [ ] 🟡 [#438 Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) — Fixed window + Counter comparison

---

## Pattern 4: Binary Search (Modified)
**Days 13–16 | ~8 Problems**

**Core idea:** Standard binary search finds a target in sorted data in O(log n). Modified binary search applies to rotated arrays, answer-space problems, or finding boundaries instead of exact values.

**When to recognize it:** Sorted (or partially sorted) array. Problem needs O(log n). "First/last occurrence," "minimum in rotated," "find peak."

**Python toolkit:**
```python
left, right = 0, len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

---

### Day 13
- [ ] 🟢 [#704 Binary Search](https://leetcode.com/problems/binary-search/) — Pure baseline, know this cold
- [ ] 🟡 [#33 Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) — Determine which half is sorted

### Day 14
- [ ] 🟡 [#153 Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) — Pivot detection
- [ ] 🟡 [#34 Find First and Last Position of Element](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) — Two separate binary searches

### Day 15
- [ ] 🟢 [#278 First Bad Version](https://leetcode.com/problems/first-bad-version/) — Binary search on answer space
- [ ] 🟡 [#74 Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) — Treat matrix as flat sorted array

### Day 16
- [ ] 🟡 [#162 Find Peak Element](https://leetcode.com/problems/find-peak-element/) — Move toward the larger neighbor
- [ ] 🟡 [#875 Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) — Binary search on the answer

---

## Pattern 5: Tree DFS
**Days 17–20 | ~8 Problems**

**Core idea:** Recursively traverse a binary tree depth-first (pre-order, in-order, or post-order). The call stack is your friend — each recursive call handles one subtree. "Process this node, then recurse left and right."

**When to recognize it:** Path sums, depth, diameter, lowest common ancestor, validating BSTs, tree shape problems.

**Python toolkit:**
```python
def dfs(node):
    if not node:
        return base_case
    left = dfs(node.left)
    right = dfs(node.right)
    return combine(left, right, node.val)
```

---

### Day 17
- [ ] 🟢 [#104 Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) — Simplest DFS — height
- [ ] 🟢 [#112 Path Sum](https://leetcode.com/problems/path-sum/) — Root-to-leaf running total

### Day 18
- [ ] 🟢 [#226 Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) — Swap children at every node
- [ ] 🟡 [#543 Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) — left depth + right depth at each node

### Day 19
- [ ] 🟡 [#100 Same Tree](https://leetcode.com/problems/same-tree/) — Parallel DFS on two trees
- [ ] 🟡 [#235 Lowest Common Ancestor of BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) — Use BST ordering to navigate

### Day 20
- [ ] 🟡 [#98 Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) — Pass down valid range bounds
- [ ] 🟡 [#124 Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) — Tricky — return vs. global max

---

## Pattern 6: Tree BFS
**Days 21–24 | ~8 Problems**

**Core idea:** Process a binary tree level by level using a queue. At each step, pop all nodes at the current level, process them, and enqueue their children for the next level.

**When to recognize it:** "Level order," "right side view," "zigzag," "minimum depth," "connect next right pointers."

**Python toolkit:**
```python
from collections import deque
queue = deque([root])
while queue:
    for _ in range(len(queue)):
        node = queue.popleft()
        # process node
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
```

---

### Day 21
- [ ] 🟡 [#102 Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) — BFS template, must know cold
- [ ] 🟢 [#111 Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/) — BFS finds shortest path first

### Day 22
- [ ] 🟡 [#199 Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) — Last node per level
- [ ] 🟡 [#103 Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) — Alternate append direction

### Day 23
- [ ] 🟡 [#116 Populating Next Right Pointers](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/) — Link nodes within a level
- [ ] 🟡 [#515 Find Largest Value in Each Tree Row](https://leetcode.com/problems/find-largest-value-in-each-tree-row/) — Max per level

### Day 24
- [ ] 🟡 [#994 Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) — Multi-source BFS (not a tree, but same mechanism)
- [ ] 🟡 [#1161 Maximum Level Sum of a Binary Tree](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/) — Sum per level, track max

---

## Pattern 7: Graph BFS/DFS
**Days 25–28 | ~8 Problems**

**Core idea:** Extend tree traversal to graphs. Graphs can have cycles, so you need a `visited` set. BFS gives shortest paths (unweighted). DFS explores connected components.

**When to recognize it:** Islands, connected components, shortest path (unweighted), flood fill, matrix traversal, detecting cycles.

**Python toolkit:**
```python
# BFS for shortest path
from collections import deque
visited = set()
queue = deque([start])
visited.add(start)
while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

# DFS for connected components
def dfs(node):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor)
```

---

### Day 25
- [ ] 🟡 [#200 Number of Islands](https://leetcode.com/problems/number-of-islands/) — DFS flood fill on a grid
- [ ] 🟡 [#733 Flood Fill](https://leetcode.com/problems/flood-fill/) — DFS color replacement

### Day 26
- [ ] 🟡 [#695 Max Area of Island](https://leetcode.com/problems/max-area-of-island/) — DFS with accumulator
- [ ] 🟡 [#994 Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) — Multi-source BFS, time-step spreading

### Day 27
- [ ] 🟡 [#133 Clone Graph](https://leetcode.com/problems/clone-graph/) — DFS + hash map for node mapping
- [ ] 🟡 [#207 Course Schedule](https://leetcode.com/problems/course-schedule/) — Cycle detection with DFS (3-color)

### Day 28
- [ ] 🟡 [#417 Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) — Reverse BFS from borders
- [ ] 🟡 [#286 Walls and Gates](https://leetcode.com/problems/walls-and-gates/) — Multi-source BFS from gates

---

## Pattern 8: Heaps / Top-K
**Days 29–32 | ~8 Problems**

**Core idea:** A heap (priority queue) gives you O(log n) insertion and O(1) peek at the min (or max). For "K largest/smallest/most frequent" problems, maintain a heap of size K rather than sorting everything.

**When to recognize it:** "K largest," "K smallest," "K most frequent," "median of a stream," "merge K sorted."

**Python toolkit:**
```python
import heapq
# Python only has min-heap
heapq.heappush(heap, val)
heapq.heappop(heap)

# Max-heap trick: negate values
heapq.heappush(heap, -val)

# K largest: maintain min-heap of size K
heap = []
for num in nums:
    heapq.heappush(heap, num)
    if len(heap) > k:
        heapq.heappop(heap)
```

---

### Day 29
- [ ] 🟢 [#703 Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) — Min-heap of size K
- [ ] 🟡 [#215 Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) — Heap or quickselect

### Day 30
- [ ] 🟡 [#347 Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) — Counter + heap
- [ ] 🟡 [#973 K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) — Heap with tuple key

### Day 31
- [ ] 🟡 [#1046 Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) — Max-heap simulation
- [ ] 🟡 [#621 Task Scheduler](https://leetcode.com/problems/task-scheduler/) — Greedy + max-heap

### Day 32
- [ ] 🔴 [#295 Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) — Two heaps (min + max)
- [ ] 🔴 [#23 Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) — Heap with (val, list_idx)

---

## Pattern 9: Backtracking
**Days 33–36 | ~8 Problems**

**Core idea:** Build solutions incrementally. At each step, try all valid choices; if a choice leads to a dead end, undo it (backtrack) and try the next one. Think of it as DFS on a decision tree you're building as you go.

**When to recognize it:** "All subsets," "all permutations," "all combinations," "word search," "N-queens." The word "all" is a strong signal.

**Python toolkit:**
```python
def backtrack(start, current):
    if base_case:
        result.append(current[:])  # snapshot — don't append the reference
        return
    for choice in choices_from(start):
        current.append(choice)      # choose
        backtrack(next_start, current)
        current.pop()               # unchoose (backtrack)
```

---

### Day 33
- [ ] 🟡 [#78 Subsets](https://leetcode.com/problems/subsets/) — All 2^n subsets, no duplicates
- [ ] 🟡 [#77 Combinations](https://leetcode.com/problems/combinations/) — Choose K from N

### Day 34
- [ ] 🟡 [#46 Permutations](https://leetcode.com/problems/permutations/) — All orderings of N elements
- [ ] 🟡 [#90 Subsets II](https://leetcode.com/problems/subsets-ii/) — Subsets with duplicate inputs

### Day 35
- [ ] 🟡 [#39 Combination Sum](https://leetcode.com/problems/combination-sum/) — Reuse allowed, unlimited
- [ ] 🟡 [#40 Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) — No reuse, skip duplicates

### Day 36
- [ ] 🟡 [#79 Word Search](https://leetcode.com/problems/word-search/) — DFS + backtrack on a grid
- [ ] 🔴 [#51 N-Queens](https://leetcode.com/problems/n-queens/) — Classic constraint backtracking

---

## Pattern 10: Dynamic Programming
**Days 37–40 | ~8 Problems**

**Core idea:** Break a problem into overlapping subproblems. Store the answer to each subproblem (memoization or tabulation) so you never recalculate it. DP = recursion + caching, or bottom-up table-filling.

**When to recognize it:** "Max/min ways to do X," "count the number of ways," "can you reach X," "optimal substructure." If a brute-force recursion would recalculate the same inputs repeatedly, DP is the answer.

**Python toolkit:**
```python
# Top-down (memoization)
from functools import lru_cache
@lru_cache(maxsize=None)
def dp(i):
    if base_case: return ...
    return combine(dp(i-1), dp(i-2))

# Bottom-up (tabulation)
dp = [0] * (n + 1)
dp[0] = base
for i in range(1, n + 1):
    dp[i] = transition(dp[i-1], ...)
```

---

### Day 37
- [x] 🟢 [#70 Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) — Fibonacci DP — simplest possible *(already solved on your profile)*
  - **Alt:** [ ] 🟢 [#746 Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) — Direct extension of Climbing Stairs, unsolved
- [ ] 🟡 [#198 House Robber](https://leetcode.com/problems/house-robber/) — Skip-one decision at each step

### Day 38
- [ ] 🟡 [#322 Coin Change](https://leetcode.com/problems/coin-change/) — Classic unbounded knapsack
- [ ] 🟡 [#300 Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) — O(n²) DP, O(n log n) with patience sort

### Day 39
- [ ] 🟡 [#152 Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) — Track both min and max (negatives flip)
- [ ] 🟡 [#416 Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) — 0/1 knapsack on a boolean table

### Day 40
- [ ] 🟡 [#1143 Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) — 2D DP table
- [ ] 🟡 [#62 Unique Paths](https://leetcode.com/problems/unique-paths/) — Grid DP, count paths

---

## Progress Tracker

| Pattern | Days | Problems (base +alt) | Done |
|---|---|---|---|
| 1. Hash Maps | 1–4 | 8 (+3 alt) | 3/8 |
| 2. Two Pointers | 5–8 | 8 (+3 alt) | 3/8 |
| 3. Sliding Window | 9–12 | 8 | 0/8 |
| 4. Binary Search | 13–16 | 8 | 0/8 |
| 5. Tree DFS | 17–20 | 8 | 0/8 |
| 6. Tree BFS | 21–24 | 8 | 0/8 |
| 7. Graph BFS/DFS | 25–28 | 8 | 0/8 |
| 8. Heaps / Top-K | 29–32 | 8 | 0/8 |
| 9. Backtracking | 33–36 | 8 | 0/8 |
| 10. Dynamic Programming | 37–40 | 8 (+1 alt) | 1/8 |
| **Total** | **40 days** | **80 base + 7 alt** | **7/80** |

*"Done" counts problems already Accepted on your LeetCode profile before this plan started. Each already-solved problem has an unsolved **Alt** problem listed directly under it — do the Alt instead of re-solving the one you've already done. Two other solved problems on your profile (#169 Majority Element, #387 First Unique Character in a String) aren't part of this plan's pattern set, so no action needed on those.*

---

## General Rules

1. **No solution before 20 minutes.** Struggle is the point. After 20 min, take a hint — not the full answer.
2. **After solving, read the editorial or top solution.** Even if yours worked, see if there's a cleaner approach.
3. **Re-solve hard problems 3 days later** without looking at your first attempt. Pattern recognition comes from repetition, not one pass.
4. **Know the time complexity of every solution you write.** Don't move on without stating it.
5. **Easy problems are not beneath you.** They teach the clean pattern form. Do them at speed.

---

*Generated for lloydvheremu — Day 1: Sept 15, 2026*
