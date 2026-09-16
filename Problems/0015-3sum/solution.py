class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        res = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1
            while l < r:
                target = nums[l] + nums[r]
                if target > -a :
                    r -= 1
                elif target < -a:
                    l += 1
                else:
                    res.append([nums[l],nums[r], a])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        
        return res
