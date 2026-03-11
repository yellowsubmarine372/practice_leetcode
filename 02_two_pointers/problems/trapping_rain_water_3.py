from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Memory: O(n) sol
        """
        # height = [0,1,0,2,1,0,1,3,2,1,2,1]
        # find maxLeft
        maxLeft = [0 for i in range(len(height))]
        maxRight = [0 for i in range(len(height))]

        p = height[0]
        maxLeft[0] = p
        for i in range(1, len(height)):
            if height[i-1] > p:
                maxLeft[i] = height[i-1]
                p = height[i-1]
            else:
                maxLeft[i] = p

        g = height[-1]
        maxRight[-1] = g
        for i in range(len(height)-2, -1, -1):
            # print(i, i+1)
            if height[i+1] > g:
                maxRight[i] = height[i+1]
                g = height[i+1]
            else:
                maxRight[i] = g
        
        ans = 0
        for i in range(0, len(height)):
            # print(maxLeft[i], maxRight[i], height[i])
            temp = min(maxLeft[i], maxRight[i])-height[i]
            if temp > 0:
                ans += temp
        
        return ans
        
height = [0,1,0,2,1,0,1,3,2,1,2,1]
sol = Solution()
print(sol.trap(height=height))