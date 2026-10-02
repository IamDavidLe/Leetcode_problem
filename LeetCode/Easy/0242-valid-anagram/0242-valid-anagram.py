class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = {}
        for c1 in s:
            count1[c1] = 1 + count1.get(c1, 0)
        
        count2 = {}
        for c2 in t:
            count2[c2] = 1 + count2.get(c2, 0)

        return count1 == count2