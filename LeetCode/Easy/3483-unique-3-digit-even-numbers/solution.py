class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        vis = [False] * 1000
        res = 0

        for i in range(n):
            if digits[i] == 0:
                continue

            for j in range(n):
                if i == j:
                    continue

                for k in range(n):
                    if j == k or i == k or digits[k] % 2 != 0:
                        continue
                    
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if not vis[num]:
                        vis[num]= True
                        res += 1
        
        return res

