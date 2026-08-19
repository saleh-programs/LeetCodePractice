# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxVal = [0]
        self.depthOfTree(root, maxVal)
        return maxVal[0]
    def depthOfTree(self,root, maxVal):
        if not root:
            return 0
        leftDepth = self.depthOfTree(root.left, maxVal)
        rightDepth = self.depthOfTree(root.right, maxVal)
        maxVal[0] = max(maxVal[0], leftDepth + rightDepth)
        return max(leftDepth, rightDepth) + 1

        