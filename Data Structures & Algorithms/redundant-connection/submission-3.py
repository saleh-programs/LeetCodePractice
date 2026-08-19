class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjList = [[] for i in range(len(edges)+1)]
        indegrees = [0] * (len(edges)+1)
        queue = deque()

        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
            indegrees[edge[0]] += 1
            indegrees[edge[1]] += 1
        for i in range(len(indegrees)):
            if indegrees[i] == 1:
                queue.append(i)

        while queue:
            node = queue.popleft() 
            indegrees[node] -= 1
            for nbr in adjList[node]:
                if indegrees[nbr] > 1:
                    indegrees[nbr] -= 1
                if indegrees[nbr] == 1:
                    queue.append(nbr)
        values = set()
        for i in range(len(indegrees)):
            if indegrees[i]:
                values.add(i)

        for i in range(len(edges)-1, -1, -1):
            if edges[i][0] in values and edges[i][1] in values:
                return edges[i]
