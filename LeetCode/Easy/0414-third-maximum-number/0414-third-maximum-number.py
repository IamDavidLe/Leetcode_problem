class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        if len(set(nums)) < 3:
            return max(nums)
        
        nums = sorted(nums, reverse = True)
        seen = set()

        count = 0
        for num in nums:
            if num not in seen:
                seen.add(num)
                count += 1

            if count == 3:
                return num
        