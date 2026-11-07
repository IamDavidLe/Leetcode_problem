
import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        # Available servers: (weight, index)
        available = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(available)

        # Busy servers: (finish_time, weight, index)
        busy = []

        res = []
        time = 0

        for j, task in enumerate(tasks):
            time = max(time, j)

            # Release servers that have completed their tasks
            while busy and busy[0][0] <= time:
                finish, weight, i = heapq.heappop(busy)
                heapq.heappush(available, (weight, i))

            # If no server is available, jump to earliest finish time
            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    finish, weight, i = heapq.heappop(busy)
                    heapq.heappush(available, (weight, i))

            # Assign task to the best available server
            weight, i = heapq.heappop(available)
            res.append(i)

            # Record when the server will become available again
            heapq.heappush(busy, (time + task, weight, i))

        return res
