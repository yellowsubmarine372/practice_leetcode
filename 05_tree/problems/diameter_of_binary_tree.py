from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        different!!!
        height = 1 + max(left, right)
        diameter = left + right
        """
        self.res = 0 # so it is accessible on the dfs()

        # return height
        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)

            # 1) and 2) are different processes
            self.res = max(self.res, left + right) # 1) this line is for calculating maxDiameter
            return 1 + max(left, right) # 2) this line is for calculating left/right subtree height - so it only chooses one
            # 1 means the edge (to left OR right - not simultaneously)
        
        dfs(root)
        return self.res
