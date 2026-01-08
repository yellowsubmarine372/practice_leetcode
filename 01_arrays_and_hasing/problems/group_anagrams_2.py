from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = defaultdict(list) # need to initialize it as list
        for i in strs:
            key = ''.join(sorted(i))
            keys[key].append(i)
        return list(keys.values())