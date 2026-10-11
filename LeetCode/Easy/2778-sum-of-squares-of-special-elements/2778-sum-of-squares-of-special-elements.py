class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        res = []
        n = len(nums)
        for i in range(n):
            if n % (i + 1) == 0:
                res.append(nums[i])
        
        return sum(d*d for d in res)
