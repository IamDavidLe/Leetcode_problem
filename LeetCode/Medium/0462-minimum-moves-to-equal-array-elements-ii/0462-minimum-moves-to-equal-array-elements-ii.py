class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        target = nums[len(nums)//2]
        res = 0
        for num in nums:
            res += abs(num - target)
        
        return res
        