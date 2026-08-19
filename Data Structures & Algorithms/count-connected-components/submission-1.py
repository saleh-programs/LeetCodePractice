class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        availableNodes = set(i for i in range(n))
        visited = set()
        result = 0
        for i in range(len(edges)):
            adjList[edges[i][0]].append(edges[i][1])
            adjList[edges[i][1]].append(edges[i][0])

        def dfs(node):
            visited.add(node)
            if node in availableNodes:
                availableNodes.remove(node)
            for nbr in adjList[node]:
                if nbr not in visited:
                    dfs(nbr)
        
        for i in range(n):
            if i in availableNodes:
                result += 1
                dfs(i)

        return result
