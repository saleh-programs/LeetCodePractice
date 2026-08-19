class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    result = max(result, dfs(i,j,grid))
        return result
                    
        
def dfs(i,j, grid):
    grid[i][j] = "X"
    neighbors = [(i+1,j),(i,j-1),(i-1,j),(i,j+1)]
    outofbounds = lambda x: x[0] < 0 or x[1] < 0 or x[0] >= len(grid) or x[1] >= len(grid[0])
    area = 1
    for nbr in neighbors:
        if outofbounds(nbr) or grid[nbr[0]][nbr[1]] != 1:
            continue
        area += dfs(nbr[0],nbr[1],grid)
    return area
    