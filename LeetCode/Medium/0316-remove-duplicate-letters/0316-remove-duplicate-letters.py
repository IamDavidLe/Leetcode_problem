class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        count = Counter(s)
        
        for c in s:
            count[c] -= 1

            if c in seen:
                continue

            while stack and c < stack[-1] and count[stack[-1]] > 0:
                leave = stack.pop()
                seen.remove(leave)
            
            seen.add(c)
            stack.append(c)
        
        return ''.join(stack)
