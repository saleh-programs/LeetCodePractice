# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.pAnc = []
        self.qAnc = []
        anc = []
        self.findLCA(root, p, q, anc)

        i = len(self.pAnc) - 1
        j = len(self.qAnc) - 1

        while True:
            if self.pAnc[i].val == self.qAnc[j].val:
                return self.pAnc[i]
            if i > j:
                i -= 1
            elif j > i:
                j -= 1
            else: 
                i -= 1
                j -= 1
        

    def findLCA(self, root: TreeNode, p: TreeNode, q: TreeNode, anc: List[int]):
        if not root:
            return
        anc.append(root)
        self.findLCA(root.left, p, q, anc)
        self.findLCA(root.right, p, q, anc)
        if p.val == root.val:
            self.pAnc = anc.copy()
        elif q.val == root.val:
            self.qAnc = anc.copy()
        anc.pop()
