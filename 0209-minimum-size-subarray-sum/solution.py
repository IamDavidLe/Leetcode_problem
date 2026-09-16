class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        cur_sum = 0
        left = 0
        result = float('inf')
        for right in range(len(nums)):
            cur_sum += nums[right]
            while cur_sum >= target:
                result = min(result, right - left + 1)
                cur_sum -= nums[left]
                left += 1

        return result if result != float('inf') else 0