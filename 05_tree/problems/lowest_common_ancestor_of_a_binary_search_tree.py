# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lca = root
        self.result = []
        
        def dfs(root, target):
            if root is None:
                return False
            if root.val == target:
                self.result.append(root)
                return True
            if dfs(root.left, target):
                self.result.append(root)
                return True
            if dfs(root.right, target):
                self.result.append(root)
                return True
            return False
        
        dfs(root, p.val)
        pParent = self.result[:]
        self.result = []

        dfs(root, q.val)
        qParent = self.result[:]
        qParentVal = []
        for node in qParent:
            qParentVal.append(node.val)

        # print(pParent, qParent)

        return next((x for x in pParent if x.val in qParentVal), None)