class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        arr = sorted(
            [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)],
            key=lambda x: x[1]
        )

        # prev[i] = index of the last interval that doesn't overlap i
        ends = [x[1] for x in arr]
        prev = []

        from bisect import bisect_left

        for i in range(n):
            l = arr[i][0]

            # Need r < l
            j = bisect_left(ends, l) - 1
            prev.append(j)

        # dp[k][i] = best (weight, indices) using first i intervals
        dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]

        for k in range(1, 5):
            for i in range(1, n + 1):
                # Don't take interval i - 1
                best = dp[k][i - 1]

                l, r, w, original_idx = arr[i - 1]

                # Take interval i - 1
                p = prev[i - 1] + 1
                old_weight, old_indices = dp[k - 1][p]

                candidate = (
                    old_weight + w,
                    tuple(sorted(old_indices + (original_idx,)))
                )

                if candidate[0] > best[0]:
                    best = candidate
                elif candidate[0] == best[0] and candidate[1] < best[1]:
                    best = candidate

                dp[k][i] = best

        return list(dp[4][n][1])