from typing import List
from collections import defaultdict

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        base = 100_003
        mod1 = 1_000_000_007
        mod2 = 1_000_000_009

        def has_unique(k: int) -> bool:
            power1 = pow(base, k, mod1)
            power2 = pow(base, k, mod2)
            hash1 = hash2 = 0
            counts = defaultdict(int)

            for i, value in enumerate(nums):
                hash1 = (hash1 * base + value) % mod1
                hash2 = (hash2 * base + value) % mod2

                if i >= k:
                    old = nums[i - k]
                    hash1 = (hash1 - old * power1) % mod1
                    hash2 = (hash2 - old * power2) % mod2

                if i >= k - 1:
                    counts[(hash1, hash2)] += 1

            return any(count == 1 for count in counts.values())

        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if has_unique(mid):
                right = mid
            else:
                left = mid + 1

        return left