
from typing import List
from heapq import heappush, heappop

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        # Two heaps: lower half and upper half
        low, high = [], []
        low_sum = high_sum = 0
        low_size = high_size = 0

        alive = [False] * n
        in_low = [False] * n

        def prune(heap):
            while heap and not alive[heap[0][1]]:
                heappop(heap)

        def balance():
            nonlocal low_sum, high_sum
            nonlocal low_size, high_size

            prune(low)
            prune(high)

            while low_size > high_size + 1:
                neg_v, idx = heappop(low)
                v = -neg_v
                low_size -= 1
                low_sum -= v

                heappush(high, (v, idx))
                in_low[idx] = False
                high_size += 1
                high_sum += v
                prune(low)

            while low_size < high_size:
                v, idx = heappop(high)
                high_size -= 1
                high_sum -= v

                heappush(low, (-v, idx))
                in_low[idx] = True
                low_size += 1
                low_sum += v
                prune(high)

        def add(i):
            nonlocal low_sum, high_sum
            nonlocal low_size, high_size

            v = nums[i]
            alive[i] = True
            prune(low)

            if not low or v <= -low[0][0]:
                heappush(low, (-v, i))
                in_low[i] = True
                low_sum += v
                low_size += 1
            else:
                heappush(high, (v, i))
                high_sum += v
                high_size += 1

            balance()

        def remove(i):
            nonlocal low_sum, high_sum
            nonlocal low_size, high_size

            alive[i] = False
            v = nums[i]

            if in_low[i]:
                low_size -= 1
                low_sum -= v
            else:
                high_size -= 1
                high_sum -= v

            prune(low)
            prune(high)
            balance()

        # Cost for every window of size x
        cost = []

        for i in range(n):
            add(i)

            if i >= x:
                remove(i - x)

            if i >= x - 1:
                median = -low[0][0]
                operations = (
                    median * low_size - low_sum
                    + high_sum - median * high_size
                )
                cost.append(operations)

        maritovexi = (nums, x, k)

        # DP: choose k non-overlapping windows
        INF = float('inf')
        prev = [0] * (n + 1)

        for _ in range(k):
            curr = [INF] * (n + 1)

            for i in range(x, n + 1):
                skip = curr[i - 1]
                take = prev[i - x] + cost[i - x]
                curr[i] = min(skip, take)

            prev = curr

        return prev[n]
