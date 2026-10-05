class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
        
        res = []
        for i in range(1, len(nums) + 1):
            if i not in seen:
                res.append(i)
        
        return res