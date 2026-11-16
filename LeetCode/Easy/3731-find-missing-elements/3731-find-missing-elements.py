class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res = []
        nums = set(nums)
        n = max(nums)
        for i in range(min(nums), n + 1):
            if i not in nums:
                res.append(i)
        
        return res