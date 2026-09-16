class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, longest, count = 0, 0, 0
        appear = set()
        for r in range(len(s)):
            while s[r] in appear:
                appear.remove(s[l])
                l += 1
                count -= 1
            
            appear.add(s[r])
            count += 1
            longest = max(longest, count)
        
        return longest