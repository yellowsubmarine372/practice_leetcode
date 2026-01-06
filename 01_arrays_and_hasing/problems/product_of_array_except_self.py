from typing import List

class Solution:
    """
    takes too long(41ms)
    19ms solution:
      main idea is prod(nums[i-1])*prod(nums[i+1]) //prod(nums[i-1]) is the prefix, and the prod(nums[i+1]) is the suffix
      so (1) calculate prefix in the result array
      (2) and calculate suffix and muliply to the result array along the way: result[i] *= suffix (then prefix * suffix)
    """
    def calculate(self, size: int, nums: List[int]) -> tuple[List[int], List[int]]:
        prefix = [1]*(size+1)
        suffix = [1]*(size+1)

        # calculate prefix
        prefix[0] = nums[0]
        for i in range(1, size):
            prefix[i] = prefix[i-1] * nums[i]

        # calculate suffix
        suffix[size-1] = nums[size-1]
        for i in range(size-1, 1, -1):
            suffix[i-1] = suffix[i] * nums[i-1]
        
        return prefix, suffix

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        size = len(nums)
        prefix, suffix = self.calculate(size, nums)
        for i in range(size):
            temp = 0
            ans.append(prefix[i-1]*suffix[i+1])
        return ans
