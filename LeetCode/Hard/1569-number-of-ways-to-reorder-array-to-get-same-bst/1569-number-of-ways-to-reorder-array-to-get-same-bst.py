from math import comb

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        def dfs(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]

            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]

            l = len(left)
            r = len(right)

            ways = comb(l + r, l)

            return (ways * dfs(left) * dfs(right)) % MOD

        return (dfs(nums) - 1) % MOD