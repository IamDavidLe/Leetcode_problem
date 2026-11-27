class Solution:
    def findGCD(self, nums: list[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)

        for i in range(max_num, 0, -1):
            if min_num % i == 0 and max_num % i == 0:
                return i
        
        