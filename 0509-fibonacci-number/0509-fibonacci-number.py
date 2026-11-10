class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        prev, curr = 0, 1
        for i in range(n-1):
            temp = curr
            curr = prev + curr
            prev = temp
        
        return curr
        