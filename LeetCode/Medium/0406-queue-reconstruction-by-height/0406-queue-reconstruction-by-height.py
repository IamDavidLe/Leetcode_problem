class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))

        res = []

        for h, k in people:
            res.insert(k, [h, k])

        return res