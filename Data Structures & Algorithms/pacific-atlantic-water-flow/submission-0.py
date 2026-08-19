class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # quick bad solution, let's see if it works
        result = []
        pacific = lambda x: x[0] < 0 or x[1] < 0
        atlantic = lambda x: x[0] >= len(heights) or x[1] >= len(heights[0])
        def bfs(i, j):
            nonlocal pacific, atlantic
            stack = [(i, j)]
            visited = {f"{i}-{j}"}

            hitAtlantic = False
            hitPacific = False

            while stack:
                r,c = stack.pop()
                neighbors = [(r+1,c), (r,c-1), (r-1,c), (r,c+1)]

                for nbr in neighbors:
                    if pacific(nbr):
                        hitPacific = True
                        continue
                    if atlantic(nbr):
                        hitAtlantic = True
                        continue
                    if f"{nbr[0]}-{nbr[1]}" not in visited and heights[nbr[0]][nbr[1]] <= heights[r][c]:
                        stack.append((nbr[0], nbr[1]))
                        visited.add(f"{nbr[0]}-{nbr[1]}")
            return hitPacific and hitAtlantic

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if bfs(r,c):
                    result.append([r,c])

        return result




                