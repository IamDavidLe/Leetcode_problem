class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        switch_on = set()
        for num in bulbs:
            if num not in switch_on:
                switch_on.add(num)
            else:
                switch_on.remove(num)
        
        return sorted(list(switch_on))
            