# Binary Trees
from collections import deque


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def __str__(self):
    return str(self.val)
  
# recursive pre order traversal (DFS)
# Time : O(n), Space: O(n)
def pre_order(node):
  if not node: # if node is null
    return
  
  # traversal : node -> left -> right
  print(node)
  pre_order(node.left) 
  pre_order(node.right)

def in_order(node):
  if not node:
    return

  # traversal : left -> node -> right
  in_order(node.left)
  print(node)
  in_order(node.right)

# not using recursive, and using iterative
# Iterative Pre Order Traversial (DFS) Time: O(n), Space: O(n)
def pre_order_iterative(node):
  stk = [node] # root

  while stk:
    node = stk.pop()
    print(node)
    if node.right: # doing right first, so left is the last item (FILO)
      stk.append(node.right)
    if node.left:
      stk.append(node.left)


# level order traversal (BFS) Time: O(n), Space: O(n)
def level_orde(node):
  q = deque()
  q.append(node)

  while q:
    node = q.popleft()
    print(node)
    if node.left:
      q.append(node.left) # FIFO
    if node.right:
      q.append(node.right)

def search(node, target):
  if not node:
    return False
  
  if node.val == target:
    return True
  
  return search(node.left, target) or search(node.right, target)

# BST
# Time: O(log n), Space: O(log n)
def search_bst(node, target):
  if not node:
    return False

  if node.val == target:
    return True
  
  # because the tree is BST, we don't have to lookup both left and right
  if target < node.val: # need to go to the smaller subtree
    return search_bst(node.left, target)
  else: # go to the bigger subtree
    return search_bst(node.right, target)