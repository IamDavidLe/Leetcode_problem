class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        char = list(s)

        for i in range(0, len(s), 2 * k):
            left = i
            right = min(i + k - 1, len(s) - 1)

            while left < right:
                char[left], char[right] = char[right], char[left]
                left += 1
                right -= 1

        return ''.join(char)