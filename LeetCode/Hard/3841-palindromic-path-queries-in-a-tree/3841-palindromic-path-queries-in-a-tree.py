
class Solution:
    def palindromePath(
        self,
        n: int,
        edges: list[list[int]],
        s: str,
        queries: list[str]
    ) -> list[bool]:

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Step 1: Find parent, depth, and DFS order
        parent = [-1] * n
        depth = [0] * n
        order = [0]

        for u in order:
            for v in graph[u]:
                if v == parent[u]:
                    continue

                parent[v] = u
                depth[v] = depth[u] + 1
                order.append(v)

        # Step 2: Compute subtree sizes and heavy children
        size = [1] * n
        heavy = [-1] * n

        for u in reversed(order):
            best = 0

            for v in graph[u]:
                if parent[v] == u:
                    size[u] += size[v]

                    if size[v] > best:
                        best = size[v]
                        heavy[u] = v

        # Step 3: Heavy-Light Decomposition
        head = [0] * n
        pos = [0] * n
        timer = 0

        for u in order:
            if parent[u] != -1 and heavy[parent[u]] == u:
                continue

            v = u

            while v != -1:
                head[v] = u
                pos[v] = timer
                timer += 1
                v = heavy[v]

        # Step 4: Build iterative Segment Tree
        base = 1

        while base < n:
            base *= 2

        seg = [0] * (2 * base)
        chars = list(s)

        def char_mask(c):
            return 1 << (ord(c) - ord('a'))

        for u in range(n):
            seg[base + pos[u]] = char_mask(chars[u])

        for i in range(base - 1, 0, -1):
            seg[i] = seg[2 * i] ^ seg[2 * i + 1]

        def update(u, c):
            chars[u] = c
            i = base + pos[u]
            seg[i] = char_mask(c)

            while i > 1:
                i //= 2
                seg[i] = seg[2 * i] ^ seg[2 * i + 1]

        def range_xor(left, right):
            left += base
            right += base
            result = 0

            while left <= right:
                if left & 1:
                    result ^= seg[left]
                    left += 1

                if not (right & 1):
                    result ^= seg[right]
                    right -= 1

                left //= 2
                right //= 2

            return result

        # Step 5: Query XOR along path u -> v
        def path_xor(u, v):
            result = 0

            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u

                result ^= range_xor(
                    pos[head[u]], pos[u]
                )

                u = parent[head[u]]

            if depth[u] > depth[v]:
                u, v = v, u

            result ^= range_xor(pos[u], pos[v])

            return result

        # Step 6: Process queries
        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                update(u, c)

            else:
                u = int(parts[1])
                v = int(parts[2])

                mask = path_xor(u, v)

                valid = (
                    mask == 0 or
                    (mask & (mask - 1)) == 0
                )

                answer.append(valid)

        return answer
