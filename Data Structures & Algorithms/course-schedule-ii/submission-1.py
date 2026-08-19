class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        indegrees = [0] * numCourses
        result = []
        for i in range(numCourses):
                graph[i]
        for i in range(len(prerequisites)):
            graph[prerequisites[i][1]].add(prerequisites[i][0])
            indegrees[prerequisites[i][0]] += 1
        
        print(graph, indegrees)

        for _ in range(len(indegrees)):
            for i in range(len(indegrees)):
                if i in graph and indegrees[i] == 0:
                    for nbr in graph[i]:
                        indegrees[nbr] -= 1
                    del graph[i]
                    result.append(i)
                    break
        if len(result) != numCourses:
            return []
        return result

