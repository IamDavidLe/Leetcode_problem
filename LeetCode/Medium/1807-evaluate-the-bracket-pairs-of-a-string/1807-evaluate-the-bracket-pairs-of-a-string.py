class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        dic = dict(knowledge)

        res = []
        i = 0

        while i < len(s):
            if s[i] == '(':
                j = i

                while s[j] != ')':
                    j += 1

                key = s[i + 1:j]
                res.append(dic.get(key, "?"))

                i = j + 1
            else:
                res.append(s[i])
                i += 1

        return "".join(res)