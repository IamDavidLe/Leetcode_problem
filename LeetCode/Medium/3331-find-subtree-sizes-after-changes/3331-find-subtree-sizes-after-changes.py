
class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n = len(parent)

        # Step 1: Build the original tree
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        # Step 2: Find the new parent for each node
        new_parent = parent.copy()
        last_seen = {}

        def dfs(node):
            char = s[node]

            # Save the previous ancestor with the same character
            prev = last_seen.get(char)

            if prev is not None:
                new_parent[node] = prev

            # Current node becomes the closest ancestor
            last_seen[char] = node

            for child in children[node]:
                dfs(child)

            # Backtrack
            if prev is None:
                del last_seen[char]
            else:
                last_seen[char] = prev

        dfs(0)

        # Step 3: Build the modified tree
        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        # Step 4: Calculate subtree sizes
        answer = [1] * n

        def calculate(node):
            for child in new_children[node]:
                calculate(child)
                answer[node] += answer[child]

        calculate(0)

        return answer
