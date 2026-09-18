class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        grid = obstacleGrid
        ROWS, COLS = len(grid), len(grid[0])
        dp = [0] * COLS
        dp[COLS - 1] = 1

        for r in reversed(range(ROWS)):
            for c in reversed(range(COLS)):
                if grid[r][c]:
                    dp[c] = 0
                
                elif c + 1 < COLS:
                    dp[c] = dp[c] + dp[c + 1]
        
        return dp[0]
