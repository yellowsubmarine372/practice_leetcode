from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        takes to much time and memory
        need to fix find-minimum-in-rotated-sorted-array algorithm first
        """
        # find the boundary
        boundary = 0
        minAns = nums[0]
        left, right = 0, len(nums)-1
        new_arr = [0 for i in range(len(nums))]

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[left]:
                if nums[left] < minAns:
                    minAns = nums[left]
                    boundary = left
                if right == mid:
                    break
                right = mid
            else: # nums[mid] > nums[right]
                if nums[right] < minAns:
                    minAns = nums[right]
                    boundary = right
                if left == mid:
                    break
                left = mid
        
        print(boundary)

        # make new array
        new_arr = nums[boundary:] + nums[:boundary]
        left, right = 0, len(new_arr)-1

        while left <= right:
            mid = (left + right) // 2
            if new_arr[mid] == target:
                return (boundary + mid) % len(new_arr)
            elif new_arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1