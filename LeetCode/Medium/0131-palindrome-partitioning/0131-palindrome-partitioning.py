class Solution:
    def partition(self, s: str) -> list[list[str]]:
        def is_palindrome(string):
            l, r = 0, len(string) - 1
            while l <= r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        res = []
        def backtracking(start, path):
            if start == len(s):
                res.append(path[:])
                return
            
            for i in range(start, len(s)):
                substring = s[start:i + 1]
                if not is_palindrome(substring):
                    continue
                
                path.append(substring)
                backtracking(i + 1, path)
                path.pop()
        
        backtracking(0, [])
        return res
