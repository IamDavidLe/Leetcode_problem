
from sortedcontainers import SortedList
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        available = SortedList(range(k))
        busy = []  # (finish_time, server_id)
        count = [0] * k

        for i, time in enumerate(arrival):

            # 1. Release servers that finished their work
            while busy and busy[0][0] <= time:
                finish_time, server = heapq.heappop(busy)
                available.add(server)

            # 2. Drop the request if all servers are busy
            if not available:
                continue

            # 3. Find the next available server
            preferred = i % k
            pos = available.bisect_left(preferred)

            # Wrap around if necessary
            if pos == len(available):
                pos = 0

            server = available[pos]

            # 4. Assign the request
            available.remove(server)
            count[server] += 1

            finish_time = time + load[i]
            heapq.heappush(busy, (finish_time, server))

        # 5. Return the busiest servers
        max_requests = max(count)

        return [i for i in range(k) if count[i] == max_requests]
