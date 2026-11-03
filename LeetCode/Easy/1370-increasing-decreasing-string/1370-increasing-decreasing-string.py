class Solution:
    def sortString(self, s: str) -> str:
        freq = [0] * 26 # represent the frequency of each character
        for char in s:
            pos = ord(char) - ord('a')
            freq[pos] += 1
        
        res = []
        while len(res) < len(s):
            for i in range(26):
                if freq[i] > 0:
                    res.append(chr(ord('a') + i))
                    freq[i] -= 1
                
            for i in range(25, -1, -1):
                if freq[i] > 0:
                    res.append(chr(ord('a') + i))
                    freq[i] -= 1
                    
        return ''.join(res)