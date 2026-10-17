class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        count = {}
        list_of_word = (s1 + ' ' + s2).split()
        for word in list_of_word:
            count[word] = 1 + count.get(word, 0)
        
        uncommon = []
        for word, time in count.items():
            if time == 1:
                uncommon.append(word)
            
        return uncommon