import time
# 6.461143493652344e-05

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        s = time.time()
        # Potentially better, more space
        pacific = lambda x: x[0] < 0 or x[1] < 0
        atlantic = lambda x: x[0] >= len(heights) or x[1] >= len(heights[0])
        statuses = {}
        result = []

        runs = 0
        def bfs(i, j):
            nonlocal pacific, atlantic, runs
            stack = [(i, j)]
            visited = {f"{i}-{j}"}
            hitAtlantic = False
            hitPacific = False


            while stack:
                runs += 1
                r,c = stack.pop()
                neighbors = [(r+1,c), (r,c-1), (r-1,c), (r,c+1)]

                for nbr in neighbors:
                    if i == 4 and j ==0:
                        print(nbr)

                    if pacific(nbr):
                        hitPacific = True
                        continue
                    if atlantic(nbr):
                        hitAtlantic = True
                        continue
                    if f"{nbr[0]}-{nbr[1]}" not in visited and heights[nbr[0]][nbr[1]] <= heights[r][c]:
                        if f"{nbr[0]}-{nbr[1]}" in statuses:
                            hitPacific = True if statuses[f"{nbr[0]}-{nbr[1]}"][0] else hitPacific
                            hitAtlantic = True if statuses[f"{nbr[0]}-{nbr[1]}"][1] else hitAtlantic
                            if hitAtlantic and hitPacific:
                                return True
                            continue
                        stack.append((nbr[0], nbr[1]))
                        visited.add(f"{nbr[0]}-{nbr[1]}")
            statuses[f"{i}-{j}"] = [hitPacific, hitAtlantic]
            return hitPacific and hitAtlantic

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if bfs(r,c):
                    result.append([r,c])

        print((time.time() - s))
        print("runs:", runs)
        return result




                