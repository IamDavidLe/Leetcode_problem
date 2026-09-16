class Solution:
    def longestPalindrome(self, s: str) -> str:
        def length(l, r):
            while (l >= 0 and r < len(s)) and s[r] == s[l] :
                l -= 1
                r += 1
            return l, r
        L, R = 0,0
        for i in range(len(s)):
            l_odd, r_odd = length(i, i)
            l_even, r_even = length(i, i+1)
            len_odd = r_odd-l_odd-1
            len_even = r_even-l_even-1
            len_max = R-L+1
            if len_odd>len_even:
                if len_max<len_odd:
                    L= l_odd+1
                    R = r_odd-1
            else:
                if len_max<len_even:
                    L= l_even+1
                    R = r_even-1
        return s[L:R + 1]    