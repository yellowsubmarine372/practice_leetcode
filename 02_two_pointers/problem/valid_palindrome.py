# isalnum
# method for determining is alphanumeric character
# if we want to find not alphanumeric char(ex. special character):
#   print([i for i in strs if not i.isalnum()])
# isalnum returns True, False (whither it is alphanumeric or not)


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = s.lower()
        cleaned_s= cleaned_s.strip()
        cleaned_s = cleaned_s.replace(' ', '')
        cleaned_s = [i for i in cleaned_s if i.isalnum()]
        if cleaned_s[::-1] == cleaned_s:
            return True
        return False
