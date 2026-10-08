class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ''
        stack = []
        openN = 0
        closeN = 0
        for bracket in s:
            stack.append(bracket)
            if bracket == '(':
                openN += 1
            else:
                closeN += 1
                
            if closeN == openN:
                stack.pop(0)
                stack.pop()
                res += ''.join(stack)
                stack = []
    
        return res