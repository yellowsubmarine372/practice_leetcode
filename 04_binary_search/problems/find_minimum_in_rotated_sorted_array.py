from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        for cases that loops = cases that are already left is equal to mid (or right = mid)
        just vary one condition in left or right: left = mid condition to left = mid + 1 (right = mid)
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        """
        minAns = nums[0]
        left, right = 0, len(nums)-1

        while left < right:
            mid = (left + right) // 2
            # print(mid, left, right)
            if nums[mid] < nums[left]:
                if nums[left] < minAns:
                    minAns = nums[left]
                if right == mid:
                    break
                right = mid
            else: # nums[mid] > nums[right]
                if nums[right] < minAns:
                    minAns = nums[right]
                if left == mid:
                    break
                left = mid

        return minAns