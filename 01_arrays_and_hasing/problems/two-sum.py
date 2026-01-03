from typing import List

class Solution:
    """
    better answer for this (22ms),
    try to find each other match (instead of focusing on one to find its match)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        for i in range(size):
            val = target - nums[i]
            for j in range(size):
                if j == i:
                    continue
                if nums[j] == val:
                    ans = [i, j]
                    return ans
                    
            
        