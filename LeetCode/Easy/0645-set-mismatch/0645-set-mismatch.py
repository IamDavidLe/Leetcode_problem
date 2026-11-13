class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        seen = set()
        dup = -1
        missing = -1

        for num in nums:
            if num in seen:
                dup = num
            seen.add(num)
        
        for i in range(1, len(nums) + 1):
            if i not in seen:
                missing = i
        
        return [dup, missing]