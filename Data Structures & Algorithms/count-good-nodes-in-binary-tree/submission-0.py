# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0
        def dfs(node, maxAncestor):
            if not node:
                return
            if maxAncestor <= node.val:
                self.good += 1

            maxAncestor = max(maxAncestor, node.val)
            dfs(node.left, maxAncestor)
            dfs(node.right, maxAncestor)

        dfs(root, root.val)
        return self.good