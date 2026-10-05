class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        l = 0
        k = len(p)

        count1 = {}
        for c in p:
            count1[c] = 1 + count1.get(c, 0)

        res = []
        count2 = {}

        for r in range(len(s)):
            count2[s[r]] = 1 + count2.get(s[r], 0)

            if (r - l + 1) > k:
                count2[s[l]] -= 1

                if count2[s[l]] == 0:
                    del count2[s[l]]

                l += 1

            if (r - l + 1) == k:
                if count1 == count2:
                    res.append(l)

        return res