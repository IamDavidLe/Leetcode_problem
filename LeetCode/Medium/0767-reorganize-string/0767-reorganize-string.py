from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        res, c = [], Counter(s)
        heap = [(-value, key) for key, value in c.items()]
        heapq.heapify(heap)
        prev_a, prev_b = 0, ''
        while heap:
            freq, letter = heapq.heappop(heap)
            res.append(letter)
            if prev_a < 0: 
                # because we don't want the letter with most freq to appear in the next position
                heapq.heappush(heap, (prev_a, prev_b))
            
            freq += 1 # we are using negative --> increment by 1 equivalent to decrement by 1
            prev_a, prev_b = freq, letter
        

        res = ''.join(res)
        return res if len(res) == len(s) else ''


            
            