class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        first_row, second_row, third_row = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
        res = []
        for word in words:
            w = set(word.lower())
            if w <= first_row or w <= second_row or w <= third_row:
                res.append(word)
        
        return res
