class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        for c in s:
            if c == '#':
                if stack1:
                    stack1.pop()
                continue
            
            stack1.append(c)

        stack2 = []
        for c in t:
            if c == '#':
                if stack2:
                    stack2.pop()
                continue
            
            stack2.append(c)
        
        return ''.join(stack1) == ''.join(stack2)