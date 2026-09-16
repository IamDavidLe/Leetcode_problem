class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        res = float('inf')
        
        for i, a in enumerate(nums):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                k = nums[l] + nums[r] + a
                if abs(k - target) < abs(res - target):
                    res = k

                if k > target:
                    r -= 1

                elif k < target:
                    l += 1

                else:
                    return k
        
        return res