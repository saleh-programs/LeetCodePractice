# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    pointer = 0
    indices = {}
    preorder = []
    inorder = []
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        for i in range(len(inorder)):
            self.indices[inorder[i]] = i 
        self.inorder = inorder
        self.preorder = preorder
        return self.buildTree2(0, len(inorder) - 1)

    def buildTree2(self, l: int, r: int) -> Optional[TreeNode]:
        if (r - l + 1) == 0: 
            return None
        elif (r - l + 1) == 1:
            self.pointer += 1
            return TreeNode(self.preorder[self.pointer - 1])

        root = TreeNode(self.preorder[self.pointer])
        root_index = self.indices[root.val]
        self.pointer += 1

        leftchild = self.buildTree2(l, root_index - 1)
        rightchild = self.buildTree2(root_index + 1, r)
        if leftchild:
            root.left = leftchild
        if rightchild:
            root.right = rightchild

        return root







        