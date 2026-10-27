class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        path = [['#' for _ in range(n)] for _ in range(m)]
        row, col = 0, 0
        path[row][col] = '.'
        while col < n and col + 1 < n:
            col += 1 
            path[row][col] = '.'
        
        while row < m and row + 1 < m:
            row += 1
            path[row][col] = '.'
        

        return [''.join(path[row]) for row in range(m)]