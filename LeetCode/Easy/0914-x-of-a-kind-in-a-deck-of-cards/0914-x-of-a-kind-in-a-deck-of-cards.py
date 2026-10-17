from math import gcd
class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        count = {}
        for num in deck:
            count[num] = 1 + count.get(num, 0)
        
        result = 0
        for freq in count.values():
            result = gcd(result, freq)
        
        return result > 1