class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        prefix = 0
        seen = {0 : -1}
        
        for i in range(len(nums)):
            prefix += nums[i]
            remainder = prefix % k

            if remainder in seen:
                if i - seen[remainder] >= 2:
                    return True
            else:
                seen[remainder] = i
        
        return False
