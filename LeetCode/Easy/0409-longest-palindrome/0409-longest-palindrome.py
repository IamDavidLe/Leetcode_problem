class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        res = 0
        has_odd = False

        for freq in count.values():
            if freq % 2 == 0:
                res += freq
            else:
                res += freq - 1
                has_odd = True

        if has_odd:
            res += 1

        return res