class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count = {}

        for row in matrix:
            pattern = tuple(x ^ row[0] for x in row)
            count[pattern] = count.get(pattern, 0) + 1

        return max(count.values())