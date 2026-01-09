from typing import List


class Solution:
    """
    takes 63ms
    look up sol that takes 38ms
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        size = len(nums)
        diff = [0]*(size-1)
        for i in range(1, size):
            diff[i-1] = nums[i] - nums[i-1]
        
        ans = 0
        max_length = 0
        start = False
        sub_length = 0
        for num in diff:
            if num == 0:
                start = True
            elif num == 1 and not start:
                sub_length = 1
                start = True
            elif num == 1 and start:
                sub_length += 1
            elif num != 1 and start:
                if sub_length > max_length:
                    max_length = sub_length
                sub_length = 0
                start = False
        if size > 0:
            return max(max_length, sub_length) + 1
        else:
            return 0