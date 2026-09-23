class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x

        if target < 0:
            return -1

        if target == 0:
            return len(nums)

        l = 0
        cur_sum = 0
        max_len = -1

        for r in range(len(nums)):
            cur_sum += nums[r]

            while cur_sum > target:
                cur_sum -= nums[l]
                l += 1

            if cur_sum == target:
                max_len = max(max_len, r - l + 1)

        if max_len == -1:
            return -1

        return len(nums) - max_len