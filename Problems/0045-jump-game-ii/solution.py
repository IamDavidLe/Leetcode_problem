class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 0
        farthest = 0
        jump = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == end:
                jump += 1
                end = farthest
        
        return jump