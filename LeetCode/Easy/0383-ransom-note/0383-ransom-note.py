class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}
        for c in ransomNote:
            count[c] = 1 + count.get(c, 0)
        
        for c1 in magazine:
            if c1 in count:
                count[c1] -= 1
                if count[c1] == 0:
                    del count[c1]
            
        return True if not count else False
