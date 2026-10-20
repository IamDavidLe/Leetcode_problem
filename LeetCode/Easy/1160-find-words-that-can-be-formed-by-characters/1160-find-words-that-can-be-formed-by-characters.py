class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        count1 = {}
        for char in chars:
            count1[char] = 1 + count1.get(char, 0)

        def check_word(sub_word):
            count = {}
            for char in sub_word:
                count[char] = 1 + count.get(char, 0)

            for c, num in count.items():
                if count1.get(c, 0) < num:
                    return False

            return True

        res = 0
        for word in words:
            if check_word(word):
                res += len(word)

        return res