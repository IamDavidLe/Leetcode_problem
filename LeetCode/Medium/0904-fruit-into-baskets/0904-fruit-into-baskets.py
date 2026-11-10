class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        l, r = 0, 0
        hashmap = {}
        max_length = 0
        while r < len(fruits):
            hashmap[fruits[r]] = 1 + hashmap.get(fruits[r], 0)
            while len(hashmap) > 2:
                hashmap[fruits[l]] -= 1
                if hashmap[fruits[l]] == 0:
                    del hashmap[fruits[l]]
                l += 1
            
            max_length = max(max_length, r - l + 1)
            r += 1
        
        return max_length
