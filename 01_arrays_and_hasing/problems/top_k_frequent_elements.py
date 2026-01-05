from typing import List 
from collections import Counter 

class Solution:
    """
    time complexity = O(Nlogn)
    1. try using heapq, than sorted
    2. and understand how .get, sorted() method worked
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums)
        ans = sorted(nums_count, key=nums_count.get, reverse=True)
        return ans[0:k]