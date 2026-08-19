class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        indegrees = [0] * n
        result = []
        for i in range(len(edges)):
            graph[edges[i][1]].append(edges[i][0])
            graph[edges[i][0]].append(edges[i][1])

        visited = set()
        amountVisited = [0]
        def dfs(node, caller):
            visited.add(node)
            amountVisited[0] += 1
            for nbr in graph[node]:
                if nbr not in visited:
                    dfs(nbr, node)
                elif nbr != caller:
                    return False
            visited.remove(node)
            return True
        for i in range(n):
            amountVisited[0] = 0     
            if not dfs(0,None):
                return False

        return amountVisited[0] == n


