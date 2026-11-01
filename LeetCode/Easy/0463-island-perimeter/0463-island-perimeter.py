class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        def dfs(row, col):
            if (row < 0 or row >= ROW or
                col < 0 or col >= COL or 
                grid[row][col] == 0):
                    return 1
            
            if grid[row][col] == -1:
                return 0
            
            grid[row][col] = -1

            return (dfs(row + 1, col) +
                    dfs(row, col + 1) + 
                    dfs(row - 1, col) + 
                    dfs(row, col - 1))
            
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    return dfs(i, j)