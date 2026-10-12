class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l, r = 0, len(s1) - 1
        count1 = {}

        for c in s1:
            count1[c] = count1.get(c, 0) + 1

        count2 = {}

        for i in range(len(s1)):
            count2[s2[i]] = 1 + count2.get(s2[i], 0)

        while r < len(s2):
            if count1 == count2:
                return True

            r += 1

            if r < len(s2):
                count2[s2[r]] = 1 + count2.get(s2[r], 0)

                count2[s2[l]] -= 1

                if count2[s2[l]] == 0:
                    del count2[s2[l]]

                l += 1

        return False