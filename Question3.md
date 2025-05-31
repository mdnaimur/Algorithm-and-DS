# Assignment Instructions & Details

This assignment is designed to strengthen your problem-solving skills across four core algorithmic paradigms: **Recursion**, **Backtracking**, **Divide and Conquer**, and **Dynamic Programming**. Through six carefully crafted problems, you will explore how to model real-world challenges using foundational algorithmic techniques, analyze and compare multiple solution strategies, and optimize for time and space complexity.

---

## Submission Guidelines

**Platform:** Submit via a public GitHub repository.

**Structure:**
- Organize folders by problem (e.g., `Problem1/`, `Problem2/`, etc.).
- Each folder should contain:
  - Source code files.
  - A `README.md` explaining:
    - Problem understanding.
    - Chosen approach and justification.
    - Time and space complexity analysis.
    - Any challenges faced and how they were overcome.
    - Diagrams or illustrations if applicable.

**Restrictions:**
- No AI tools (e.g., ChatGPT) are allowed. Submissions suspected of AI assistance will be rejected.
- Code must be original and written by the student.

---

## Part 1: Recursive Thinking (30 Marks)

### Problem 1: The Mysterious Sequence (15 Marks)

You are given a sequence defined recursively as follows:

```
S(1) = 1  
S(2) = 2  
S(n) = S(n - 1) + 2 * S(n - 2) for n > 2
```

**Tasks:**
- Implement a recursive function to compute `S(n)`.
- Analyze the time and space complexity of your implementation.
- Optimize your solution using memoization.
- Further optimize using an iterative approach (tabulation).
- Compare and contrast the three approaches in terms of efficiency.

---

### Problem 2: The Tower of Hanoi with a Twist (15 Marks)

In the classic Tower of Hanoi problem, you move disks from one peg to another, following specific rules. Now, suppose you have an additional constraint:

> You can only move disks to **adjacent pegs** (e.g., from peg A to B, or B to C, but not A to C directly).

**Tasks:**
- Implement a recursive solution for this modified problem.
- Determine the minimum number of moves required for `n` disks.
- Analyze the time complexity.
- Discuss how this constraint changes the problem compared to the classic version.

---

## Part 2: Backtracking Challenges (35 Marks)

### Problem 3: The Constrained Maze (20 Marks)

You are given a 2D grid representing a maze with the following:

- `0`: Open path  
- `1`: Wall  
- `2`: Start point  
- `3`: End point  

You can move in four directions (up, down, left, right), but with constraints:
- You **cannot move in the same direction more than twice consecutively**.
- You must reach the end point in the **shortest path possible** under this constraint.

**Tasks:**
- Implement a backtracking solution to find the shortest path.
- Analyze the time and space complexity.
- Discuss how the added constraint affects the complexity and solution approach.

---

### Problem 4: The Subset Sum Puzzle (15 Marks)

Given a set of positive integers and a target sum, determine all subsets that sum up to the target. Constraints:
- Each number can be used **at most once**.
- Subsets must be in **non-descending order**.

**Tasks:**
- Implement a backtracking solution to find all valid subsets.
- Ensure that the subsets are printed in **lexicographical order**.
- Analyze the time and space complexity.

---

## Part 3: Dynamic Strategies (35 Marks)

### Problem 5: The Optimal Path (20 Marks)

You are given a grid of size `m x n`, where each cell contains a non-negative integer representing the cost to enter that cell. Starting from the top-left cell, you need to reach the bottom-right cell with the **minimum total cost**. You can only move **right or down** at any point.

**Tasks:**
- Implement a recursive solution to find the minimum cost path.
- Optimize your solution using dynamic programming (tabulation).
- Analyze the time and space complexity of both approaches.
- Discuss the trade-offs between the recursive and DP solutions.

---

### Problem 6: The Longest Common Subsequence (15 Marks)

Given two strings, find the length of their **longest common subsequence (LCS)**.

**Tasks:**
- Implement a recursive solution to compute the LCS length.
- Optimize your solution using dynamic programming.
- Analyze the time and space complexity.
- Discuss how the DP approach improves efficiency over recursion.

---

## Evaluation Criteria

| Criteria                          | Marks |
|----------------------------------|-------|
| Correctness of Solutions         | 40    |
| Efficiency and Optimization      | 20    |
| Code Quality and Documentation   | 15    |
| Complexity Analysis and Justification | 15 |
| Creativity and Problem Understanding | 10 |
| **Total**                        | **100** |

---

## Additional Notes

- Ensure your code is clean, well-commented, and follows best practices.
- Use diagrams or flowcharts where they can aid understanding.
- Reflect on each problem:
  - What did you learn?
  - What challenges did you face?
