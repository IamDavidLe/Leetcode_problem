class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = {0 : 0}
        prefix = 0
        max_length = 0
        for i, num in enumerate(nums, 1):
            if num == 0:
                prefix -= 1
            elif num == 1:
                prefix += 1
            
            if prefix in count:
                max_length = max(max_length, i - count[prefix])
            else:
                count[prefix] = i
        
        return max_length
