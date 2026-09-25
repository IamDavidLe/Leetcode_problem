class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        i = 0

        def parse():
            nonlocal i

            res = set()
            cur = {""}

            while i < len(expression) and expression[i] != "}":

                if expression[i] == ",":
                    res |= cur
                    cur = {""}
                    i += 1

                elif expression[i] == "{":
                    i += 1

                    nxt = parse()

                    i += 1  # skip }

                    cur = {
                        a + b
                        for a in cur
                        for b in nxt
                    }

                else:
                    char = expression[i]
                    i += 1

                    cur = {
                        word + char
                        for word in cur
                    }

            return res | cur

        return sorted(parse())