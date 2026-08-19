class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        m = len(beginWord)
        graph = {word: set() for word in wordList}
        graph[beginWord] = set()

        for word1 in graph.keys():
            for word2 in graph.keys():
                if word1 == word2 or word1 in graph[word2]:
                    continue 
                wrong = 0
                for i in range(m):
                    if word1[i] != word2[i]:
                        wrong += 1
                if wrong == 1:
                    graph[word1].add(word2)
                    graph[word2].add(word1)

        queue = deque([(beginWord,0)])
        visited = set()
        
        while queue:
            node, pathLength = queue.popleft()
            for nbr in graph[node]:
                if nbr == endWord:
                    return (pathLength + 1) + 1 
                if nbr not in visited:
                    queue.append((nbr, pathLength + 1))
                    visited.add(nbr)
        return 0
                    
    
                    
