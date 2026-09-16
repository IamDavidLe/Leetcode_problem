class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin, curMax, res = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            if num < 0:
                curMin, curMax = curMax, curMin
            
            curMax = max(num, curMax * num)
            curMin = min(num, curMin * num)

            res = max(curMax, res)
        return res