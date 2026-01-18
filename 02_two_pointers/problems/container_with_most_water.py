from typing import List


class Solution:
    """
    takes 9 seconds...
    but at least I solved it on my own
    """
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        size = len(height)
        nums = []
        for i, a in enumerate(height):
            nums.append([i, a])
        nums.sort(key= lambda x : x[1])

        for i in range(size):
            index, min_height = nums[i][0], nums[i][1]
            max_height = 0
            width = 0
            l, r = 0, size-1
            while max_height < min_height:
                if (index-l) >= (r-index):
                    max_height = height[l]
                    width = index-l
                    l+=1
                else:
                    max_height = height[r]
                    width = r-index
                    r-=1
            area = min_height*width
            if area > max_area:
                max_area = area
        return max_area
    

nums = [1,8,6,2,5,4,8,3,7]
# nums = [1, 1]
# nums = [1,2,4,3]
sol = Solution()
print(sol.maxArea(nums))