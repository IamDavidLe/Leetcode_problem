class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        res = []
        def backtracking(start, path):
            if len(path) >= 2:
                res.append(path[:])
            
            seen = set()

            for i in range(start, len(nums)):
                if nums[i] in seen:
                    continue
                
                if path and nums[i] < path[-1]:
                    continue
                
                seen.add(nums[i])
                path.append(nums[i])
                backtracking(i + 1, path)
                path.pop()
        
        backtracking(0, [])
        return res
