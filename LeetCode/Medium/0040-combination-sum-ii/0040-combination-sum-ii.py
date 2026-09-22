class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates = sorted(candidates)
        def backtracking(cur_sum, path, start):
            if cur_sum == target:
                res.append(path[:])
            if cur_sum > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                num = candidates[i]
                path.append(num)
                backtracking(cur_sum + num, path, i + 1)
                path.pop()
            
        backtracking(0, [], 0)
        return res