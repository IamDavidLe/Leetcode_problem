class Solution:
    def findLucky(self, arr: list[int]) -> int:
        count = {}
        for num in arr:
            count[num] = 1 + count.get(num, 0)
        
        largest, res = 0, 0
        for freq, num in count.items():
            if freq == num and num > largest:
                res = num
                largest = num
        
        return res if res != 0 else -1