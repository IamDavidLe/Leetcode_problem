class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        target = len(nums) // 2
        res = 0
        for num in nums:
            res += abs(num - nums[target])
        
        return res