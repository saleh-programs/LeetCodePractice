# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder = []
        def dfs(node):
            if not node:
                return True
            
            left = dfs(node.left)
            if inorder:
                if node.val <= inorder[-1]:
                    return False
            inorder.append(node.val)
            right = dfs(node.right)
            return left and right
        return dfs(root)