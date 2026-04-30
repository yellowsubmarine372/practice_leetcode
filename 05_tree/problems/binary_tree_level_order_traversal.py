from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        self.result = []
        def bfs(start):
            queue = deque([start])

            while queue:
                temp = []
                for _ in range(len(queue)):
                    node = queue.popleft()
                    temp.append(node.val)

                    if node.left is not None:
                        queue.append(node.left)
                    if node.right is not None:
                        queue.append(node.right)
                self.result.append(temp)
        if root is not None:
            bfs(root)
        
        return self.result