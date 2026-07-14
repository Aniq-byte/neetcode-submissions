class Solution:
    def dfs(self, grid, i, j):
        if grid[i][j] == "1":
            grid[i][j] = "0"
            grid = self.dfs(grid, max(i-1, 0), j)
            grid = self.dfs(grid, min(i+1, len(grid)-1), j)
            grid = self.dfs(grid, i, min(j+1,len(grid[0])-1))
            gird = self.dfs(grid, i, max(j-1,0))

        return grid

    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    grid = self.dfs(grid, i, j)
        
        return count
        