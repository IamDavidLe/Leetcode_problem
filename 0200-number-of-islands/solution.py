class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        count = 0
        def backtracking(r, c):
            if r < 0 or r >= ROW or c < 0 or c >= COL or grid[r][c] != '1':
                return
            
            grid[r][c] = '0' # Mark the spot
            backtracking(r + 1, c)
            backtracking(r - 1, c)
            backtracking(r, c + 1)
            backtracking(r, c - 1)

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == '1':
                    backtracking(r,c)
                    count += 1
        
        return count