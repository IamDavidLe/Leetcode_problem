class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        res = []
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                res.append(num)
        
        return res