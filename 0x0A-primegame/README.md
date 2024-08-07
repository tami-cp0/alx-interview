# Prime Game

## Overview

The Prime Game is a two-player game where players alternately select prime numbers from a set of integers starting from 1 up to a given number \( n \). Each chosen prime number and its multiples are removed from the set. The player who cannot make a move loses. This game is played for multiple rounds, and the player who wins the most rounds is declared the overall winner.

## Problem Statement

Given a number of rounds and a list where each element represents the maximum number \( n \) for each round, determine who wins the most rounds assuming both players play optimally.

- **Maria** always goes first.
- **Ben** goes second.
- Both players play optimally.

## Function Prototype

```python
def isWinner(x: int, nums: List[int]) -> str:
Parameters
x (int): The number of rounds.
nums (List[int]): A list where each element represents the maximum number 
𝑛
n for each round.
Returns
str: The name of the player who won the most rounds. If there is a tie or if no player won any rounds, return None.
Example
python
Copy code
x = 3
nums = [4, 5, 1]

print(isWinner(x, nums))  # Output: Ben
```

Explanation
Round 1:

Set: {1, 2, 3, 4}
Maria picks 2, removing {2, 4}.
Ben picks 3, removing {3}.
Ben wins as Maria has no moves left.
Round 2:

Set: {1, 2, 3, 4, 5}
Maria picks 2, removing {2, 4}.
Ben picks 3, removing {3}.
Maria picks 5, removing {5}.
Maria wins as Ben has no moves left.
Round 3:

Set: {1}
Maria has no primes to pick.
Ben wins by default.
Ben wins 2 out of 3 rounds.
