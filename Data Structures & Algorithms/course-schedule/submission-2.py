class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(set)
        visited = set()

        def dfs(node):
            visited.add(node)
            for adj in graph[node]:
                if adj in visited:
                    return False
                elif not dfs(adj):
                    return False
            visited.remove(node)
            return True
            

        # create the graph
        for i in range(numCourses):
            graph[i]
        for each in prerequisites:
            graph[each[1]].add(each[0])
        
        for node in graph.keys():
            if not dfs(node):
                return False
        return True



