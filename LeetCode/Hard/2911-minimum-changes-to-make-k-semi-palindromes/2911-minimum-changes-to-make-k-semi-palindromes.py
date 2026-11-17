class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        inf = float("inf")

        divisors = [[] for _ in range(n + 1)]
        for d in range(1, n // 2 + 1):
            for length in range(2 * d, n + 1, d):
                divisors[length].append(d)

        cost = [[inf] * (n + 1) for _ in range(n)]
        for start in range(n):
            for end in range(start + 2, n + 1):
                part = s[start:end]

                for d in divisors[end - start]:
                    changes = 0
                    for offset in range(d):
                        group = part[offset::d]
                        for i in range(len(group) // 2):
                            changes += group[i] != group[-1 - i]

                    cost[start][end] = min(cost[start][end], changes)

        dp = [[inf] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for parts in range(1, k + 1):
            for end in range(2 * parts, n + 1):
                # Chừa ít nhất 2 ký tự cho mỗi đoạn trước và đoạn cuối.
                for start in range(2 * (parts - 1), end - 1):
                    dp[parts][end] = min(
                        dp[parts][end],
                        dp[parts - 1][start] + cost[start][end],
                    )

        return dp[k][n]