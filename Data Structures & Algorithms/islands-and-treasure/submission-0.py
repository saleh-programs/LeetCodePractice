class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        def bfs(i,j):
            queue = deque([(i,j,0)])
            visited = {f"{i}-{j}"}
            while queue:
                x, y, path = queue.popleft()
                print(x,y,path)

                neighbors = [(x+1,y), (x, y-1),(x-1,y),(x,y+1)]
                outofbounds = lambda x: x[0] < 0 or x[1] < 0 or x[0] >= len(grid) or x[1] >=len(grid[0])
                for nbr in neighbors:
                    if outofbounds(nbr) or f"{nbr[0]}-{nbr[1]}" in visited or grid[nbr[0]][nbr[1]] == -1:
                        continue
                    if grid[nbr[0]][nbr[1]] == 0:
                        return path+1
                    queue.append((nbr[0],nbr[1],path+1))
                    visited.add(f"{nbr[0]}-{nbr[1]}")

            return -1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0 and grid[i][j] != -1:
                    grid[i][j] = bfs(i,j)
                
