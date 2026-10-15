class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        level = 0
        res = 0
        while level <= n:
            for i in range(level, n):
                k = len(set(nums[level:i+1]))
                res += k * k
            level += 1

        return res
