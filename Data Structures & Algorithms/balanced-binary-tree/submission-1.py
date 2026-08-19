# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left = self.findHeight(root.left)
        right = self.findHeight(root.right)
        if abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False
        
    def findHeight(self, root):
        if not root:
            return -1
        left = self.findHeight(root.left)
        right = self.findHeight(root.right)
        return max(left, right) + 1