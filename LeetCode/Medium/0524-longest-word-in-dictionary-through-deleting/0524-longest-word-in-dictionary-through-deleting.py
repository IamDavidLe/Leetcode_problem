class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        dictionary.sort()
        longest = 0
        res = ''
        for word in dictionary:
            pnt1, pnt2 = 0, 0
            while pnt2 < len(word) and pnt1 < len(s):
                if word[pnt2] == s[pnt1]:
                    pnt1 += 1
                    pnt2 += 1
                else:
                    pnt1 += 1
            
            if pnt2 == len(word) and len(word) > longest:
                res = word
                longest = len(word)
        
        return res
