class Solution:
    def findLHS(self, nums: list[int]) -> int:
        nums.sort()
        l = 0
        longest = 0

        for r in range(1, len(nums)):
            while nums[r] - nums[l] > 1:
                l += 1

            if nums[r] - nums[l] == 1:
                longest = max(longest, r - l + 1)
            

        return longest