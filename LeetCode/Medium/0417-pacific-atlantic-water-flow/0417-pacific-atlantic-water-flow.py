class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        ROW, COL = len(heights), len(heights[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        pacific, atlantic = set(), set()

        def dfs(row, col, visited):
            visited.add((row, col))
            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if (0 <= nr < ROW and 0 <= nc < COL and (nr, nc) not in visited and 
                    heights[row][col] <= heights[nr][nc]):
                        dfs(nr, nc, visited)
            
            
        # Checking Pacific
        for row in range(ROW):
            dfs(row, 0, pacific)
        
        for col in range(COL):
            dfs(0, col, pacific)
        
        # Checking Atlantic
        for row in range(ROW):
            dfs(row, COL - 1, atlantic)
        
        for col in range(COL):
            dfs(ROW - 1, col, atlantic)
        
        res = []
        for r in range(ROW):
            for c in range(COL):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        
        return res