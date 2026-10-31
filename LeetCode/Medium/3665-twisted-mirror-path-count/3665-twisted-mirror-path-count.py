class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        right = [[0] * n for _ in range(m)]
        down = [[0] * n for _ in range(m)]

        # Starting point
        if m == 1 and n == 1:
            return 1

        if n > 1:
            right[0][1] = 1

        if m > 1:
            down[1][0] = 1

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue

                from_left = right[r][c]
                from_above = down[r][c]

                if grid[r][c] == 1:
                    # Moving right into mirror -> down
                    if r + 1 < m:
                        down[r + 1][c] = (
                            down[r + 1][c] + from_left
                        ) % MOD

                    # Moving down into mirror -> right
                    if c + 1 < n:
                        right[r][c + 1] = (
                            right[r][c + 1] + from_above
                        ) % MOD

                else:
                    total = (from_left + from_above) % MOD

                    if c + 1 < n:
                        right[r][c + 1] = (
                            right[r][c + 1] + total
                        ) % MOD

                    if r + 1 < m:
                        down[r + 1][c] = (
                            down[r + 1][c] + total
                        ) % MOD

        if grid[m - 1][n - 1] == 1:
            return 0

        return (
            right[m - 1][n - 1] +
            down[m - 1][n - 1]
        ) % MOD