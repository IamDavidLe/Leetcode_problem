class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            stack.append(c)
            
            if len(stack) >= 3 and ''.join(stack[-3:]) == 'abc':
                for _ in range(3):
                    stack.pop()
                
        return len(stack) == 0
