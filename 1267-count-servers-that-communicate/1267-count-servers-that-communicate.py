class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        rows = [sum(row) for row in grid] # number of servers on each row
        cols = [sum(col) for col in zip(*grid)] # number of servers on each col
        
        count = 0
        for i, row in enumerate(grid):
            for j, server in enumerate(row):
                num = rows[i] + cols[j]
                if server and num > 2:
                    count += 1
        
        return count