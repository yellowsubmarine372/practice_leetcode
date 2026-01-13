from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        This is a wrong solution and should fail because of time complexity
        It was accepted only because the test cases didn’t cover this case
        don’t try to solve it using the remainder approach (fixing one index and looping over the other)
        you need to move both indices (start and end)
        """
        start = 0
        size = len(numbers)
        for start in range(size - 1):
            remain = target - numbers[start]
            end = size - 1 # changed index, to make it start from the last
            # but starting end from size + 1, is same as starting from size - 1 
            #  because it all has to see one element at a time
            while end > start:
                if numbers[end] > remain:
                    end -= 1
                elif numbers[end] == remain:
                    return [start + 1, end + 1]
                else:
                    break