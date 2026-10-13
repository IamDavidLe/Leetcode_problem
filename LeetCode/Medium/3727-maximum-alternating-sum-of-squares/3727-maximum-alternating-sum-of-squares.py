class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        new_list = []
        for num in nums:
            if num < 0:
                num = abs(num)
            new_list.append(num)
        
        new_list.sort()
        res = 0
        l, r = 0, len(new_list) - 1
        while l < r:
            res += new_list[r] ** 2 - new_list[l] ** 2
            l += 1
            r -= 1
        
        if len(new_list) % 2 == 1:
            res += new_list[l] ** 2
        
        return res