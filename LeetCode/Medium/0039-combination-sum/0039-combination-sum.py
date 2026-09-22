class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        def backtracking(cur_sum, path, start):
            if cur_sum == target:
                res.append(path[:])
                return
            if cur_sum > target:
                return
            for i in range(start, len(candidates)):
                num = candidates[i]

                path.append(num)
                backtracking(cur_sum + num, path, i)
                path.pop()
                
        backtracking(0, [], 0)
        return res