from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True

        def dfs(root: Optional[TreeNode]):
            if not root:
                return 0

            leftHight = dfs(root.left)
            rightHight = dfs(root.right)

            if abs(leftHight - rightHight) > 1:
                self.res = False
                return 0

            return 1 + max(leftHight, rightHight)

        dfs(root)
        return self.res