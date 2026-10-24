class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix[0]) - 1
        while l < r:
            top, bottom = l, r
            for i in range(r - l):
                topleft = matrix[top][l + i]

                matrix[top][l + i] = matrix[bottom - i][l]

                matrix[bottom - i][l] = matrix[bottom][r - i]

                matrix[bottom][r - i] = matrix[top + i][r]

                matrix[top + i][r] = topleft
            
            l += 1
            r -= 1


