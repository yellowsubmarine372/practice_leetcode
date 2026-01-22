class Solution:
    """
    4ms
    it can be more simlified
    you only have to check closing brackets
    """
    def isValid(self, s: str) -> bool:
        d = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        a = list(s)

        key = a.pop()
        if key not in d.keys():
            return False
        temp = [d[key]]

        while a:
            key = a.pop()
            if temp and key == temp[-1]:
                temp.pop()
            else:
                if key not in d.keys():
                    return False
                temp.append(d[key])
        if temp:
            return False
        return True