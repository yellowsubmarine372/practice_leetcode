class Solution:
    def isPalindrome(self, x: int) -> bool:
        arr2 = []
        while x>=1:
            arr2.append(x%10)
            x = x//10
        arr = arr2[::-1]
        if x>=0 and arr == arr2:
            return True
        return False