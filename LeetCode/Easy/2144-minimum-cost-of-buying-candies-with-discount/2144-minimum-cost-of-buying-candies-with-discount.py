class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        cost.sort(reverse= True)
        n = len(cost)
        res = 0
        for i in range(n):
            if (i + 1) % 3 == 0:
                continue
            
            res += cost[i]

        return res