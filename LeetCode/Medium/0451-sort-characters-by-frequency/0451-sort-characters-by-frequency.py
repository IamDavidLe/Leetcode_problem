class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}

        for c in s:
            count[c] = 1 + count.get(c, 0)

        chars = sorted(count, key=lambda c: count[c], reverse=True)

        res = ""
        for c in chars:
            res += c * count[c]

        return res