class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        pointer1 = pointer2 = 0
        count = 0
        while pointer1 < len(g) and pointer2 < len(s):
            if g[pointer1] <= s[pointer2]:
                count += 1
                pointer1 += 1
                pointer2 += 1
            else:
                pointer2 += 1

        return count