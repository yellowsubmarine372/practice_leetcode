# import uuid
# my_uuid = uuid.uuid4()

from typing import List
import uuid

class Solution:
    
    def __init__(self) -> None:
        self.uuid = str(uuid.uuid4())
        self.uuid_2 = str(uuid.uuid4())

    def encode(self, strs: List[str]) -> str:
        length = len(strs)
        if length == 0:
            return self.uuid
        elif length == 1:
            return strs[0]
        temp = ''
        for i in range(length):
            if strs[i] == "":
                strs[i] = self.uuid_2
        return self.uuid.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == self.uuid:
            return []
        ans = list(s.split(self.uuid))
        length = len(ans)
        for i in range(length):
            if ans[i] == self.uuid_2:
                ans[i] = ''
        return ans
        

sol = Solution()

nums = [["Hello","World"], ["Hello World","World"], [""], [], ["",""]]
for i in nums:
  temp = sol.encode(i)
  print(temp)
  print(sol.decode(temp))
  print("")


