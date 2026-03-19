class TreeNode:
  def __init__(self, data, left, right):
    self.data = data
    self.left = left
    self.right = right
    
# all the same pattern
# Note: Recursive pattern always have to return same type

def treeSum(root):
  if root is None:
    return 0
  leftSum = treeSum(root.left)
  rightSum = treeSum(root.right)
  
  return (root.data + leftSum + rightSum) # subtree sum return to the parent node -> goes on -> unitl it sums all in the root

def treeMax(root):
  if root is None:
    return float("-inf")
  leftMax = treeMax(root.left)
  rightMax = treeMax(root.right)
  return max(root.data, leftMax, rightMax)

def treeHeight(root):
  if root is None:
    return 0
  leftHeight = treeHeight(root.left)
  rightHeight = treeHeight(root.right)
  return (1 + leftHeight + rightHeight) # including root(1)

def existsinTree(root, value):
  if root is None:
    return False
  leftExists = existsinTree(root.left, value)
  rightExists = existsinTree(root.right, value)
  return (root.data == value or leftExists or rightExists)

def reverseTree(node):
  ...