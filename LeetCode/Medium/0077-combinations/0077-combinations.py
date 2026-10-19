class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        def backtracking(start, path):
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(start, n + 1):
                path.append(i)
                backtracking(i + 1, path)
                path.pop()
            
        backtracking(1, [])
        return res