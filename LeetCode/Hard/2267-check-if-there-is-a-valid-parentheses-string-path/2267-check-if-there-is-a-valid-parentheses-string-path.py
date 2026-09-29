class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        ROWS = len(grid)
        COLS = len(grid[0])

        # Valid parentheses string must have even length
        if (ROWS + COLS - 1) % 2 == 1:
            return False

        if grid[0][0] != '(' or grid[-1][-1] != ')':
            return False

        memo = {}

        def dfs(r, c, balance):
            if r >= ROWS or c >= COLS:
                return False

            if grid[r][c] == '(':
                balance += 1
            else:
                balance -= 1

            # Too many closing parentheses
            if balance < 0:
                return False

            remaining = (ROWS - 1 - r) + (COLS - 1 - c)

            # Not enough cells left to close all '('
            if balance > remaining:
                return False

            if r == ROWS - 1 and c == COLS - 1:
                return balance == 0

            state = (r, c, balance)

            if state in memo:
                return memo[state]

            memo[state] = (
                dfs(r + 1, c, balance) or
                dfs(r, c + 1, balance)
            )

            return memo[state]

        return dfs(0, 0, 0)