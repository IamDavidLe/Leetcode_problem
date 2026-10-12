
class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        count = [0] * 30

        # Count set bits at each position
        for num in nums:
            for bit in range(30):
                if num & (1 << bit):
                    count[bit] += 1

        ans = 0

        # Construct k numbers greedily
        for _ in range(k):
            x = 0

            for bit in range(30):
                if count[bit] > 0:
                    x |= (1 << bit)
                    count[bit] -= 1

            ans = (ans + x * x) % MOD

        return ans
