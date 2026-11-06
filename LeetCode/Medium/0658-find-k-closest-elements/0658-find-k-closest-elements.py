import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = [] # tuple of (distance and num)
        for num in arr:
            heapq.heappush(heap, (abs(x - num), num))
        
        res = []
        for _ in range(k):
            distance, num = heapq.heappop(heap)
            res.append(num)

        return sorted(res)