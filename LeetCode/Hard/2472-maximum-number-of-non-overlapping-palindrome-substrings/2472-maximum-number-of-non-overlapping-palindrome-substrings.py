class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]
        for length in range(1, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                is_palindrome[left][right] = s[left] == s[right] and (length <= 2
                or is_palindrome[left+1][right-1])
        
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i-1]
            for left in range(i):
                if is_palindrome[left][i - 1] and i - left >= k:
                    dp[i] = max(dp[i], dp[left] + 1)
        
        return dp[n]
                
            

