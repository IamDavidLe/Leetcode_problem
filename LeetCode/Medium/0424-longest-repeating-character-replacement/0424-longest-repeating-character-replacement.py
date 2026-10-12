class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0 
        longest = 0 
        count = {}
        while r < len(s):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_freq = max(count.values())
            
            if (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
            r += 1
            
        return longest