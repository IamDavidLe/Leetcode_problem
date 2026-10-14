class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        for char in "!?',;.":
            paragraph = paragraph.replace(char, " ")
            
        words = paragraph.split()
        count = {}
        for word in words:
            count[word.lower()] = 1 + count.get(word.lower(), 0)

        for ban in banned:
            count.pop(ban, None)
        
        res = ''
        most_freq = 0
        for word, time in count.items():
            if time > most_freq:
                res = word
                most_freq = time
        
        return res