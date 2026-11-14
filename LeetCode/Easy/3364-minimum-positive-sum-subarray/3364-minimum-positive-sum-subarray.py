class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        best = float('inf')
        for j in range(l, n + 1):
            for length in range(l, min(r, j) + 1):
                s = prefix[j] - prefix[j - length]
                if 0 < s < best:
                    best = s
        return -1 if best == float('inf') else best