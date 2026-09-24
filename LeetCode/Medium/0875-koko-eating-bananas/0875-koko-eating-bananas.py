class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            total_time = 0
            eat_speed = (l + r) // 2
            for i in piles:
                total_time += math.ceil(i/eat_speed)
            if total_time > h:
                l = eat_speed + 1
            else:
                r = eat_speed - 1
        
        return l
                