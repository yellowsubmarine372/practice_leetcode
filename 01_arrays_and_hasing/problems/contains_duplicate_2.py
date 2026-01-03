from typing import List
    
# looking one by one; it's faster when you only need to find exception
class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp = set()

        for i in nums:
            if i in temp: # it means that we already have that elemeent
                return True
            temp.append(i)
        return False