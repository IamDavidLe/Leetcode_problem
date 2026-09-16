class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        dp = [[0] * (k + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = 1

        for j in range(1, k + 1):
            prefix = 0

            for i in range(n):
                # prefix = dp[0][j-1] + ... + dp[i-1][j-1]
                dp[i][j] = prefix

                # Không tạo segment kết thúc tại i
                if i > 0:
                    dp[i][j] += dp[i - 1][j]

                dp[i][j] %= MOD

                # Sau khi tính dp[i][j],
                # mới thêm nó vào prefix cho i tiếp theo
                prefix += dp[i][j - 1]
                prefix %= MOD

        return dp[n - 1][k]