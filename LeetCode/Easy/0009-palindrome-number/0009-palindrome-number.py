class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        reversed_num = a[::-1]
        if reversed_num == a:
            return True
        return False
