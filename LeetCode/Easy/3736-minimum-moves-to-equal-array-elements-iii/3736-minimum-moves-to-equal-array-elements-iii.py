class Solution:
    def minMoves(self, nums: List[int]) -> int:
        res = 0
        target = max(nums)
        for num in nums:
            res += abs(target - num)
        
        return res