class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {'M' : 1000, 'D' : 500, 'C' : 100, 'L' : 50,
                    'X' : 10, 'V' : 5, 'I' : 1}
        
        res = 0
        for n in range(1, len(s)):
            if hashmap[s[n - 1]] >= hashmap[s[n]]:
                res += hashmap[s[n-1]]
            else:
                res -= hashmap[s[n-1]]
        
        return res + hashmap[s[-1]]