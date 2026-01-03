class Solution:
    """
    too complex code design
    importing libraries is faster
    or try using defaultdict(int) next time (*it initializes to 0)
    """
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        for word in s:
            if word in s_count.keys(): # O(1)
                s_count[word] += 1
            else:
                s_count[word] = 1
        t_count = {}
        for word in t:
            if word in t_count.keys(): # O(1)
                t_count[word] += 1
            else:
                t_count[word] = 1

        diff = s_count.items() ^ t_count.items()
        if not diff:
            return True
        return False
          
            