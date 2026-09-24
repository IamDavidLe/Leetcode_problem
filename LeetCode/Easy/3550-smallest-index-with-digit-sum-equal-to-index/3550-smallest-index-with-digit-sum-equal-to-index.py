class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, val in enumerate(nums):
            if val < 9:
                if i == val:
                    return i
            
            else:
                check = str(val)
                total = 0
                for num in check:
                    total += int(num)
                if total == i:
                    return i
        
        return -1
                
