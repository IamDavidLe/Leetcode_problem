class Solution:
    def maxProduct(self, n: int) -> int:
        digits = []
        temp = n
        while temp > 0:
            val = temp % 10
            digits.append(val)
            temp //= 10
        
        max_prod = 0
        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                max_prod = max(max_prod, digits[i] * digits[j])

        return max_prod