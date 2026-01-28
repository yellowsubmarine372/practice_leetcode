from typing import List


class Solution:
    """
    Know It's wrong, but couldn't figure out sol to how to remember index
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0 for i in range(len(temperatures))]
        stack = []
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                k = stack[-1][1]
                ans[k] = i-k
                stack.pop()
            stack.append([temperatures[i], i])
        return ans
