class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        res = 0
        max_val = 0
        for i, val in enumerate(arr):
            max_val = max(max_val, val)
            if i == max_val:
                res += 1
        
        return res