# Note:
# divison that truncate toward zero (int(a/b) method) :
#   if divison is positive value -> a//b acts as floor
#   if divison is negative value -> a//b acts as ceiling
# but a//b allways operates as a floor

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = ['+', '-', '*', '/']
        num = []
        ans = int(tokens[0])
        for i in range(len(tokens)):
            t = tokens[i]
            if t in op:
                n2, n1 = num.pop(), num.pop()
                if t == '+':
                    ans = (n1 + n2)
                elif t == '-':
                    ans = (n1 - n2)
                elif t == '*':
                    ans = (n1 * n2)
                elif t == '/':
                    ans = int(n1 / n2)
                num.append(ans)
            else:
                num.append(int(t))
        return ans