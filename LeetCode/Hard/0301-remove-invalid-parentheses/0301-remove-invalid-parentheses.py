from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(string):
            balance = 0

            for c in string:
                if c == '(':
                    balance += 1
                elif c == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        queue = deque([s])
        visited = {s}
        result = []

        while queue:
            size = len(queue)

            for _ in range(size):
                curr = queue.popleft()

                if is_valid(curr):
                    result.append(curr)
                    continue

                for i in range(len(curr)):
                    if curr[i] not in "()":
                        continue

                    new_string = curr[:i] + curr[i + 1:]

                    if new_string not in visited:
                        visited.add(new_string)
                        queue.append(new_string)

            if result:
                return result