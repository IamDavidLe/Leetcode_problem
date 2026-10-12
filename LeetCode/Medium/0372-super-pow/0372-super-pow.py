class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        MOD = 1337
        num_b = int(''.join(map(str,b)))

        def recursion(x, n):
            if n == 0:
                return 1
            
            res = recursion(x, n // 2)
            res = (res * res) % MOD

            return res if n % 2 == 0 else (x * res) % MOD
        
        res = recursion(a % MOD, num_b)
        return res