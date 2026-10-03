class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        word_to_pattern = {}
        pattern_to_word = {}

        for i in range(len(words)):
            word = words[i]
            char = pattern[i]

            if word in word_to_pattern:
                if word_to_pattern[word] != char:
                    return False
                
            else:
                word_to_pattern[word] = char
            
            if char in pattern_to_word:
                if pattern_to_word[char] != word:
                    return False
                
            else:
                pattern_to_word[char] = word
            
        return True
