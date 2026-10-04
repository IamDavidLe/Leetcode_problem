class Solution:
    def checkValidString(self, s: str) -> bool:
        low = high = 0

        for char in s:
            if char == '(':
                low += 1
                high += 1

            elif char == ')':
                low -= 1
                high -= 1

            else:  # '*'
                low -= 1      # treat '*' as ')'
                high += 1     # treat '*' as '('

            if high < 0:
                return False

            low = max(low, 0)

        return low == 0