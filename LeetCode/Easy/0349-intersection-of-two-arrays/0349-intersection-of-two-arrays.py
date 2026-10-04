class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        seen = set()
        for num1 in nums1:
            if num1 not in seen:
                seen.add(num1)
        
        res = set()    
        for num2 in nums2:
            if num2 in seen:
                res.add(num2)
            
        return list(res)
    