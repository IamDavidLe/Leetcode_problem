class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(', 
        '}':'{', 
        ']':'['}
        stack = []

        for c in s:
            if c not in dic:
                stack.append(c)
            else:
                if not stack:
                    return False
                
                if stack[-1] != dic[c]:
                    return False
                
                stack.pop()
            
        return len(stack) == 0
