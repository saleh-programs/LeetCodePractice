class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # test, wanna see if they'd put no fresh bananas
        queue = deque([])
        visited = set()
        bananas = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    bananas += 1
                if grid[i][j] == 2:
                    queue.append((i,j,0))

        maxMinutes = 0
        while queue:
            x, y, minutes = queue.popleft()
            neighbors = [(x+1,y),(x,y-1),(x-1,y),(x,y+1)] 
            outofbounds = lambda x: x[0] < 0 or x[1] < 0 or x[0] >= len(grid) or x[1] >= len(grid[0])

            for nbr in neighbors:
                if outofbounds(nbr) or grid[nbr[0]][nbr[1]] == 0 or grid[nbr[0]][nbr[1]] == 2:
                    continue
                queue.append((nbr[0],nbr[1],minutes+1))
                grid[nbr[0]][nbr[1]] = 2
                bananas -= 1
                maxMinutes = max(maxMinutes, minutes+1)
        if bananas > 0:
            return -1
        return maxMinutes 

                
        
        
        
        return minutes
        