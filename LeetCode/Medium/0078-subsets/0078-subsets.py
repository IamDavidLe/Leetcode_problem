class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        def backtracking(start, path):
            res.append(path[:])
            if len(path) == len(nums):
                return
            

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtracking(i + 1, path)
                path.pop()
        
        backtracking(0, [])
        return res
            