from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # stored in pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height*(i - index)) # starts from the latest item index -> current index "i" (because it's no incremental anymore)
                start = index
            stack.append((start, h)) # if is incremental -> append
        for i, h in stack:
            maxArea = max(maxArea, h*(len(heights)- i)) # left overs just need to compute to the end (i -> end of heights)
        return maxArea