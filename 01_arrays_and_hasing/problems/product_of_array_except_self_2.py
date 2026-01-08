from typing import List

class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n[i-1:] * n[:i+1]

        # calculate prefix
        size = len(nums)
        result = [1]
        nums.append(1)
    
        for i in range(1, size+1):
            result.append(result[i-1]*nums[i-1])
        
        ans=[]
        suffix = 1
        for i in range(size, 0, -1):
            suffix = suffix * nums[i] 
            ans.append(suffix*result[i-1])
        return ans[::-1]

sol2 = Solution2()
print(sol2.productExceptSelf(nums= [-1,1,0,-3,3]))

        


            
        
