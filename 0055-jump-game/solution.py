class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pointer = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= pointer:
                pointer = i
        
        return True if pointer == 0 else False