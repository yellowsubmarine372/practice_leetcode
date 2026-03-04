import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = math.ceil(sum(piles) / h)
        right = max(piles)
        ans = right

        if len(piles) == 1:
            ans = left
            return ans

        while left <= right:
            mid = (right+left)//2
            k = 0
            for pile in piles:
                k += math.ceil(pile / mid)
            if k <= h:
                ans = min(mid, ans)
                right = mid - 1
            else: # k > h
                left = mid + 1

        return ans 