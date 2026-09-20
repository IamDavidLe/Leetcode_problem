class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        stack = []

        def backtracking(closeN, openN):
            if closeN == openN == n:
                res.append(''.join(stack))
                return
            
            if openN <= n:
                stack.append('(')
                backtracking(closeN, openN + 1)
                stack.pop()

            if closeN < openN:
                stack.append(')')
                backtracking(closeN + 1, openN)
                stack.pop()

        backtracking(0, 0)
        return res