# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #alt solution
        def dfs(node, maxAncestor):
            if not node:
                return 0
            points = 0
            if maxAncestor <= node.val:
                points = 1

            maxAncestor = max(maxAncestor, node.val)
            return dfs(node.left, maxAncestor) + dfs(node.right, maxAncestor) + points

        
        return dfs(root, root.val)