class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            pos = 1<<i
            if pos & n == pos:
                count += 1
            
        return count