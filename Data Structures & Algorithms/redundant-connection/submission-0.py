class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjList = [[] for i in range(len(edges)+1)]
        visited = set()
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        def dfs(node, caller):
            visited.add(node)
            for nbr in adjList[node]:
                if nbr not in visited:
                    res = dfs(nbr, node)
                    if res:
                        return res
                elif nbr != caller:
                    return (min(node,nbr), max(node,nbr))
            visited.remove(node)
            return tuple()

        def reverseDfs(node, caller):
            visited.add(node)
            for i in range(len(adjList[node])-1,-1,-1):
                nbr = adjList[node][i]
                if nbr not in visited:
                    res = dfs(nbr, node)
                    if res:
                        return res
                elif nbr != caller:
                    return (min(node,nbr), max(node,nbr))
            visited.remove(node)
            return tuple()

        options = set()
        for i in range(1,len(edges)+1):
            visited.clear()
            value = dfs(i,None)
            if value:
                options.add(value)
            visited.clear()
            value = reverseDfs(i,None)
            if value:
                options.add(value)
        for i in range(len(edges)-1,-1,-1):
            val = (edges[i][0], edges[i][1])
            if val in options:
                return edges[i]
