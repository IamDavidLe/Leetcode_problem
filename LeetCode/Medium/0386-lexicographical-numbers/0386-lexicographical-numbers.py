class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        res = []
        def dfs(cur):
            if cur > n:
                return
            res.append(cur)

            for i in range(10):
                new_cur = cur * 10 + i
                dfs(new_cur)
        
        for i in range(1, 10):
            dfs(i)

        return res