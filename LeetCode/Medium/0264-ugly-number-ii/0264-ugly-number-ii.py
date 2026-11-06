import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        seen = {1}
        for _ in range(n - 1):
            current = heapq.heappop(heap)
            for factor in (2,3,5):
                new = factor * current
                if new not in seen:
                    seen.add(new)
                    heapq.heappush(heap, new)
                
        return heapq.heappop(heap)
