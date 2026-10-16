class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> list[int]:
        X, Y, res = [1], [1], []

        while X[-1] < bound and x != 1:
            X.append(X[-1] * x)
        
        while Y[-1] < bound and y != 1:
            Y.append(Y[-1] * y)
        
        c = itertools.product(X, Y)
        for i, j in c:
            if i + j <= bound:
                res.append(i + j)
        
        return list(set(res))