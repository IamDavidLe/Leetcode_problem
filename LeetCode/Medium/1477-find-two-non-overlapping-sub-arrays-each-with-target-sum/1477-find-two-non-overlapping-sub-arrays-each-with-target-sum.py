class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)

        best = [float('inf')] * n

        l = 0
        cur_sum = 0
        shortest = float('inf')
        ans = float('inf')

        for r in range(n):
            cur_sum += arr[r]

            while cur_sum > target:
                cur_sum -= arr[l]
                l += 1

            if cur_sum == target:
                length = r - l + 1

                if l > 0:
                    ans = min(ans, length + best[l - 1])

                shortest = min(shortest, length)

            best[r] = shortest

        return -1 if ans == float('inf') else ans