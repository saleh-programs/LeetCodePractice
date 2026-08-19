
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        land = set()
        island = set()
        result = 0
        def dfs(i,j):
            neighbors = [(i+1,j),(i,j-1),(i-1,j),(i,j+1)]
            island.add(f"{i}-{j}")
            outofbounds = lambda item: item[0] < 0 or item[1] < 0 or item[0] >= len(grid) or item[1] >= len(grid[0])
            for nbr in neighbors:
                if outofbounds(nbr) or grid[nbr[0]][nbr[1]] == "0" or f"{nbr[0]}-{nbr[1]}" in island:
                    continue
                if f"{nbr[0]}-{nbr[1]}" in land or not dfs(nbr[0],nbr[1]):
                    return False
            return True
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0" or f"{i}-{j}" in land:
                    continue
                island.clear()
                if dfs(i,j):
                    land = land.union(island)
                    result += 1
            

        return result
