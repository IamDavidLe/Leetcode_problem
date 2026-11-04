class Solution:
    def digit_sum(self, n):
        s = 0
        while n != 0 :
            s += n % 10
            n //= 10
        
        return s

    def countLargestGroup(self, n: int) -> int:
        dig_sum = [0] * 37
        for i in range(1, n + 1):
            val = self.digit_sum(i)
            dig_sum[val] += 1

        size_max, count = 0, 0 
        for num in dig_sum:
            if num > size_max:
                size_max = num
                count = 1
            
            elif num == size_max:
                count += 1
        
        return count 

    