class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        ans = float('inf')
        k = nums.index(0)

        # Case 1: Increasing circular order
        if all(nums[(i + 1) % n] == (nums[i] + 1) % n
               for i in range(n)):

            ans = min(ans, k, n - k + 2)

        # Case 2: Decreasing circular order
        if all(nums[(i + 1) % n] == (nums[i] - 1) % n
               for i in range(n)):

            cost1 = 1 + (k + 1) % n
            cost2 = n - k

            ans = min(ans, cost1, cost2)

        return ans if ans != float('inf') else -1