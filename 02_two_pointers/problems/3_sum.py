from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        if failes, wrong ans.
        """
        size = len(nums)
        result = []
        nums.sort()
        start = 0 
        end = size - 1

        while start < end:
            middle = start + 1 # idk what value to initialize middle
            while middle < end:
              temp = nums[start] + nums[middle] + nums[end]
              if temp < 0:
                  middle += 1
              elif temp > 0:
                break
              else:
                  result.append([nums[start], nums[middle], nums[end]])
                  middle += 1

            if temp <= 0:
                start += 1
            elif temp > 0:
                end -= 1
                
        
        ans = []
        for a in result:
            a.sort()
            if a not in ans:
                ans.append(a)
        return ans
        
nums = [-1,0,1,2,-1,-4]
sol = Solution()
print(sol.threeSum(nums))