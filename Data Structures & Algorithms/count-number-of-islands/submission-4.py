import sys
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Better Solution
        result = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and grid[i][j] != "X":
                    count = 0
                    dfs(i,j, grid)
                    result += 1

        return result
def dfs(i,j, grid):
    neighbors = [(i+1,j),(i,j-1),(i-1,j),(i,j+1)]
    grid[i][j] = "X"
    outofbounds = lambda item: item[0] < 0 or item[1] < 0 or item[0] >= len(grid) or item[1] >= len(grid[0])
    isValid = True
    for nbr in neighbors:
        if outofbounds(nbr) or grid[nbr[0]][nbr[1]] != "1":
            continue
        dfs(nbr[0],nbr[1], grid)
