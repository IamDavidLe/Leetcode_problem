class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                inside = stack.pop()
                stack[-1] += max(inside*2, 1)
        
        return stack[-1]
