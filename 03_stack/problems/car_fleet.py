from typing import List


class Solution:
  def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    pair = [[p, s] for p, s in zip(position, speed)] # list comprehension
    stack = []

    for p, s in sorted(pair)[::-1]:
      a = (target - p)/s
      if stack and a <= stack[-1]:
        stack.pop()
    return len(stack)