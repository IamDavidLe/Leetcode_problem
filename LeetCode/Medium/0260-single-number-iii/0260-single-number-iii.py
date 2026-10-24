class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        diff = 0 
        for num in nums:
            diff ^= num
        
        mask = diff & -diff # which bit of that two numbers are different
        a, b = 0, 0
        for num in nums:
            if num & mask: # if that num has the same 1 at that position of mask
                a ^= num 
            else: # if it's not
                b ^= num
        
        return [a, b]