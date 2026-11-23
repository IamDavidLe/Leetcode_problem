class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        count = 0
        for substring in patterns:
            if len(substring) <= len(word):
                for i in range(len(word) - len(substring) + 1):
                    if substring == word[i:i+len(substring)]:
                        count += 1
                        break
        
        return count