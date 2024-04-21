<details>
<summary>1. Josephus Problem</summary>

The Josephus problem is a famous theoretical problem in mathematics and computer science. It goes as follows:

Suppose there are n people standing in a circle, numbered from 1 to n. Starting from person 1, a process eliminates every kth person around the circle until only one person remains. The goal is to determine the position of the last person remaining.

This problem has applications in various areas, including computer science, game theory, and cryptography. It is often used to illustrate concepts such as recursion, mathematical induction, and modular arithmetic.

### Example
Let's illustrate the Josephus problem with an example:

Suppose there are 7 people standing in a circle, and we eliminate every 3rd person:

1. Start with person 1.
2. Eliminate person 3 (1, 2, 3, 4, 5, 6, 7).
3. Eliminate person 6 (1, 2, 3, 4, 5, 6, 7).
4. Eliminate person 2 (1, 2, 4, 5, 6, 7).
5. Eliminate person 7 (1, 2, 4, 5, 6, 7).
6. Eliminate person 5 (1, 2, 4, 5, 6, 7).

The last person remaining is person 4.

### Solving the Problem
The Josephus problem can be solved using various approaches, including:

- **Iterative Simulation**: Simulating the elimination process until only one person remains.
- **Mathematical Formulas**: Deriving formulas to directly compute the position of the last person.
- **Recursive Algorithms**: Implementing recursive algorithms to solve the problem efficiently.
  
### Implementation
Python implementation of the Josephus problem using recursion:

```python
def josephus(n, k):
    if n == 1:
        return 1
    return (josephus(n - 1, k) + k - 1) % n + 1

# Example:
n = 7  # Number of individuals
k = 3  # Elimination interval
print("Last survivor's position:", josephus(n, k))
```

This implementation efficiently computes the position of the last person remaining in the circle.

### Conclusion
The Josephus problem is a fascinating and classic problem with diverse applications and solutions. It provides valuable insights into algorithmic thinking and computational complexity analysis.

</details>
