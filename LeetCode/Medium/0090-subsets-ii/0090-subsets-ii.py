class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        def backtracking(start, path):
            res.append(path[:])
            if len(path) == len(nums):
                return
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                path.append(nums[i])
                backtracking(i + 1, path)
                path.pop()
        
        backtracking(0, [])
        return res