class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        l = 0
        count = {}

        for r in range(10, len(s) + 1):
            substring = s[l:r]

            if substring not in count:
                count[substring] = 1
            else:
                count[substring] += 1

            l += 1

        res = []
        for string, val in count.items():
            if val >= 2:
                res.append(string)

        return res