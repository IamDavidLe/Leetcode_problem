class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashtable = {'2' : 'abc', '3' : 'def', '4' : 'ghi',
                        '5' : 'jkl', '6' : 'mno', '7' : 'pqrs',
                        '8' : 'tuv', '9' : 'wxyz'}
        res = []
        
        def backtracking(s, index):
            nonlocal res
            if len(s) == len(digits):
                res.append(s)
                return 

            for char in hashtable[digits[index]]:
                backtracking(s + char, index + 1)

        backtracking('', 0)
        return res
