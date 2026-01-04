# Enumerate Example 

# seasons = ['Spring', 'Summer', 'Fall', 'Winter']

# for index, season in enumerate(seasons):
#     print(f"Index {index}: {season}")

from typing import List

class Solution2:
    """
    better answer than sol1
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       seen = {}

       for i, num in enumerate(nums):
           if (target-num) in seen:
              return [seen[target-num], i]
           seen[num] = i