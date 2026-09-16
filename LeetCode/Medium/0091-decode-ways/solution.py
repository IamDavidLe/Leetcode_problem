class Solution:
    def numDecodings(self, s: str) -> int:
        base = {len(s) : 1}

        def dfs(i):
            if i in base:
                return base[i]
            if s[i] == '0':
                return 0
            
            res = dfs(i + 1)
            if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and
            s[i+1] in '0123456')):
                res += dfs(i+2)
            
            base[i] = res
            return res
        
        return dfs(0)