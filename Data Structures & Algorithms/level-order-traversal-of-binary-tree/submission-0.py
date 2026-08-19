from collections import deque, defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        levels = {}
        queue = deque()
        queue.append((root, 0))
        while queue:
            node, depth = queue.popleft()
            if node == None:
                continue
            if depth not in levels:
                levels[depth] = [node.val]
            else:
                levels[depth].append(node.val)
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))
        return list(levels.values())
        