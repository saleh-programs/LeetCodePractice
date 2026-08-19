class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjList = [[] for i in range(len(edges)+1)]
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        visited = set()
        stack = []
        def dfs(node, caller):
            visited.add(node)
            stack.append(node)
            for nbr in adjList[node]:
                if nbr not in visited:
                    if not dfs(nbr,node):
                        return False
                elif nbr != caller:
                    stack.append(nbr)
                    return False
            visited.remove(node)
            stack.pop()
            return True

        dfs(1,None)
        for i in range(len(stack)):
            if stack[i] == stack[-1]:
                break
            visited.remove(stack[i])
        print(visited)
        for i in range(len(edges)-1, -1,-1):
            if edges[i][0] in visited and edges[i][1] in visited:
                return edges[i]
