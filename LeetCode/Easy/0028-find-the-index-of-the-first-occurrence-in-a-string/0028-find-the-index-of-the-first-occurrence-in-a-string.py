class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = 0
        if len(needle) > len(haystack):
            return -1 

        if len(haystack) == 1 and (haystack == needle):
            return 0

        for r in range(len(needle), len(haystack) + 1):
            if needle == haystack[l:r]:
                return l
            l += 1
        
        return -1
