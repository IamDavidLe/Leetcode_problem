
class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if (r < 0 or r >= m or
                c < 0 or c >= n or
                grid[r][c] == 1):
                return

            # Mark the land as visited
            grid[r][c] = 1

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Step 1: Remove islands touching boundaries
        for r in range(m):
            if grid[r][0] == 0:
                dfs(r, 0)
            if grid[r][n - 1] == 0:
                dfs(r, n - 1)

        for c in range(n):
            if grid[0][c] == 0:
                dfs(0, c)
            if grid[m - 1][c] == 0:
                dfs(m - 1, c)

        # Step 2: Count remaining islands
        res = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    res += 1
                    dfs(r, c)

        return res
