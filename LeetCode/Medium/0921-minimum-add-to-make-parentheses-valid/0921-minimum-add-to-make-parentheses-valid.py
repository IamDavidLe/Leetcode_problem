class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        bracket = {')' : '('}
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if stack and bracket[c] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(c)

        return len(stack)