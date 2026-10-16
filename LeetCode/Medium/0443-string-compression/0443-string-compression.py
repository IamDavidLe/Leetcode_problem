class Solution:
    def compress(self, chars: list[str]) -> int:
        l, r = 0, 0
        res = []
        while l < len(chars):
            count = 0
            res.append(chars[l])

            while r < len(chars) and chars[r] == chars[l]:
                count += 1
                r += 1
            
            l = r
            if count > 1:
                res.extend(str(count))

        chars[:] = res
        return len(res)

