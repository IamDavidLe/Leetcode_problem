class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        res = [[float('inf')] * (COLS + 1) for _ in range(ROWS + 1)]
        res[ROWS][COLS - 1] = 0

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1 , -1, -1):
                plus_min = min(res[r][c + 1], res[r + 1][c])
                res[r][c] = grid[r][c] + plus_min
            
        return res[0][0]
