from collections import Counter
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        more simpler answer:
            all the anagrams can be defined as a same key (when it is sorted)
            Then you only have to check if the key from this word is in the former keys group
        """
        to_count = []
        ans = []
        size = len(strs)
        visited = [0]*size

        for word in strs:
            c = Counter(word)
            to_count.append(c)

        for i in range(size):
            result = []
            if visited[i]:
                continue
            result.append(strs[i])
            visited[i] = 1
            j = 0
            while j < size:
                if visited[j] == 0:
                    if to_count[i].items() == to_count[j].items():
                        result.append(strs[j])
                        visited[j] = 1
                j+=1
            ans.append(result)
        
        return ans
    
# strs = ["",""]
# sol = Solution()
# sol.groupAnagrams(strs)