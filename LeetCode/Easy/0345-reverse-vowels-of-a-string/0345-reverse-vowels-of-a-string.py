class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            if s[left].lower() in 'aeiou' and s[right].lower() in 'aeiou':
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

            elif s[left].lower() not in 'aeiou':
                left += 1

            elif s[right].lower() not in 'aeiou':
                right -= 1

        return ''.join(s)