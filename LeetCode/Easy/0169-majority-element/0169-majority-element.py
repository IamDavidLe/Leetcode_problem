class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        times = len(nums) // 2
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        res = 0
        appear = 0
        for val, occur in count.items():
            if occur >= times and occur > appear:
                appear = occur 
                res = val
        
        return res