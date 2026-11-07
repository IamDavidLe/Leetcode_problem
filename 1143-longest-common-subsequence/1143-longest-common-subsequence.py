class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        grid = [[0] * (m + 1) for _ in range(n + 1)]
        
        for j in range(m + 1):
            grid[0][j] = 0
        
        for i  in range(n + 1):
            grid[i][0] = 0
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[j-1] == text2[i-1]:
                    grid[i][j] = 1 + grid[i-1][j-1]
                
                else:
                    grid[i][j] = max(grid[i-1][j], grid[i][j-1])
        
        return grid[n][m]