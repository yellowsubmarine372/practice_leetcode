from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        # search through columns 
        for i in range(len(matrix)-1):
            if matrix[i][0] == target:
                return True
            if matrix[i][0] < target and matrix[i+1][0] > target:
                arr = matrix[i]
                break
        if not arr:
            arr = matrix[len(matrix)-1]

        # search through row
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (right+left)//2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False