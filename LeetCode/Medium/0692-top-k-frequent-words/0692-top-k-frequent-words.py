class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        count = {}
        for word in words:
            count[word] = 1 + count.get(word, 0)

        res = []
        for _ in range(k):
            most_freq = 0
            chosen = ''
            for word, time in count.items():
                if time > most_freq:
                    chosen = word
                    most_freq = time

                elif time == most_freq and word < chosen:
                    chosen = word

            res.append(chosen)
            del count[chosen]
        
        return res