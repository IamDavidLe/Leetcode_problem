class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = 0
        l = 0
        shortest = float('inf')
        min_l, min_r = 0, 0
        for r in range(len(s)):
            if s[r] == '1':
                ones += 1
                while ones >= k:
                    curr_len = r - l + 1
                    if (r - l + 1 < shortest) or (r - l + 1 == shortest and 
                    s[l:r + 1] < s[min_l:min_r + 1]):
                        shortest = r - l + 1
                        min_l = l
                        min_r = r 
                    if s[l] == '1':
                        ones -= 1
                    l += 1

        return s[min_l : min_r + 1] if shortest != float('inf') else ""