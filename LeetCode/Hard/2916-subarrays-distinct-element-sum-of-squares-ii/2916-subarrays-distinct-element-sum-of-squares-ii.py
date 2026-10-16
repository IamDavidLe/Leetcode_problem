
class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        tree_sum = [0] * (4 * n)
        tree_sq = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, left, right, val):
            length = right - left + 1

            tree_sq[node] = (
                tree_sq[node]
                + 2 * val * tree_sum[node]
                + val * val * length
            ) % MOD

            tree_sum[node] = (
                tree_sum[node] + val * length
            ) % MOD

            lazy[node] += val

        def push(node, left, right):
            if lazy[node] == 0 or left == right:
                return

            mid = (left + right) // 2

            apply(node * 2, left, mid, lazy[node])
            apply(node * 2 + 1, mid + 1, right, lazy[node])

            lazy[node] = 0

        def update(node, left, right, ql, qr):
            if qr < left or right < ql:
                return

            if ql <= left and right <= qr:
                apply(node, left, right, 1)
                return

            push(node, left, right)

            mid = (left + right) // 2

            update(node * 2, left, mid, ql, qr)
            update(node * 2 + 1, mid + 1, right, ql, qr)

            tree_sum[node] = (
                tree_sum[node * 2]
                + tree_sum[node * 2 + 1]
            ) % MOD

            tree_sq[node] = (
                tree_sq[node * 2]
                + tree_sq[node * 2 + 1]
            ) % MOD

        last_seen = {}
        ans = 0

        for r, num in enumerate(nums):
            p = last_seen.get(num, -1)

            update(1, 0, n - 1, p + 1, r)

            ans = (ans + tree_sq[1]) % MOD

            last_seen[num] = r

        return ans
