class Solution:
    def reverseBits(self, n: int) -> int:
        a = list(bin(n)[2:])
        a = list('0' * (32 - len(a))) + a
        
        for i in range(16): # we only go through half of the binary
            a[i], a[31 - i] = a[31 - i], a[i]
        
        return int(''.join(a), 2)