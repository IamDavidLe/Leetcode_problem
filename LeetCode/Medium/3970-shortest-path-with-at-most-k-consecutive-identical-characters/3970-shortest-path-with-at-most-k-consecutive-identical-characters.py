
import heapq

class Solution:
    def shortestPath(
        self,
        n: int,
        edges: List[List[int]],
        labels: str,
        k: int
    ) -> int:

        graph = [[] for _ in range(n)]

        # Step 1: Build directed graph
        for u, v, w in edges:
            graph[u].append((v, w))

        if k < 1:
            return -1

        # Step 2: Distance for each (node, count)
        dist = {(0, 1): 0}

        # Heap: (cost, node, consecutive_count)
        min_heap = [(0, 0, 1)]

        # Step 3: Modified Dijkstra
        while min_heap:
            cost, u, count = heapq.heappop(min_heap)

            # Skip outdated states
            if cost != dist.get((u, count)):
                continue

            # First valid destination is optimal
            if u == n - 1:
                return cost

            # Step 4: Explore neighbors
            for v, w in graph[u]:

                if labels[u] == labels[v]:
                    next_count = count + 1
                else:
                    next_count = 1

                if next_count > k:
                    continue

                new_cost = cost + w
                state = (v, next_count)

                # Relax edge
                if new_cost < dist.get(state, float('inf')):
                    dist[state] = new_cost

                    heapq.heappush(
                        min_heap,
                        (new_cost, v, next_count)
                    )

        return -1
