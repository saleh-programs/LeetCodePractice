"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        visited = {}

        def dfs(curr):
            newNode = Node(curr.val)
            visited[curr] = newNode

            for nbr in curr.neighbors:
                if nbr not in visited:
                    newNode.neighbors.append(dfs(nbr))
                else:
                    newNode.neighbors.append(visited[nbr])


            return newNode
        return dfs(node)
                                    