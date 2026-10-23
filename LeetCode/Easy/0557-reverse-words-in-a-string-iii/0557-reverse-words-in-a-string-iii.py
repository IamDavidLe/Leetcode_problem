class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        for i in range(len(words)):
            char = list(words[i])
            words[i] = ''.join(char[::-1])
        
        return ' '.join(words)