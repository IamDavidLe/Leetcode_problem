class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        pre = [1] * (len(nums) + 1)
        suf = [1] * (len(nums) + 1)
        res = []

        for i in range(1, len(nums)):
            pre[i] = pre[i-1] * nums[i-1]
        for j in range(len(nums) - 1, 0, -1):
            suf[j] = suf[j + 1] * nums[j]
        
        for i in range(len(nums)):
            res.append(pre[i] * suf[i + 1])

        return res

