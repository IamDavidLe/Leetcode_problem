class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for level in range(n):
            seen = set()

            for i in range(level, n):
                seen.add(nums[i])
                k = len(seen)
                res += k*k
        
        return res
