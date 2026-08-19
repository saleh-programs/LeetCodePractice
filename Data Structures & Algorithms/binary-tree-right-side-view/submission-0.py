from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = set()
        result = []
        queue = deque()
        queue.append((root, 0))
        while queue:
            node, depth = queue.popleft()
            if not node:
                continue
            if depth not in levels:
                levels.add(depth)
                result.append(node.val)

            queue.append((node.right, depth + 1))
            queue.append((node.left, depth + 1))
        return result
