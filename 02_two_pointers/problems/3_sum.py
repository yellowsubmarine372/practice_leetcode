# ref: https://www.youtube.com/watch?v=jzZsG8n2R9A

from typing import List


class Solution:
    """
    main idea: fix one item 
    -> and only apply start, end in 2 items 
    don't think about moving start, middle, end all 3 items simultaneously
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]: # sort -> and skip duplicated start item (not reusing the same value)
                continue
            l, r = i+1, len(nums) - 1

            # fixing one item -> and implementing two sum ii solution for middle, and end element
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    ans.append([a, nums[l], nums[r]])
                    l += 1 # if you only move left pointer, anyway it won't work, becuase we already find the answer and updating just one value would break the sum zero
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                    while nums[r] == nums[r+1] and l < r:
                        r -= 1
        return ans