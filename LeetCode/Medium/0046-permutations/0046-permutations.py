class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = [] 
        def backtracking(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backtracking(path)
                path.pop()
        
        backtracking([])
        return res