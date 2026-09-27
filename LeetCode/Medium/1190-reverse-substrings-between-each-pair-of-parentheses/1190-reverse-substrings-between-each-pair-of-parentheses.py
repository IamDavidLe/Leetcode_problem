class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        pair = [0] * n
        st = []
        for i in range(n):
            if s[i] == '(':
                st.append(i)
            elif s[i] == ')':
                j = st.pop()
                pair[i] = j
                pair[j] = i

        res = []
        direction, i = 1, 0
        while 0 <= i < n:
            if s[i] in '()':
                i = pair[i]
                direction = -direction
            
            else:
                res.append(s[i])
            
            i += direction
        
        return "".join(res)