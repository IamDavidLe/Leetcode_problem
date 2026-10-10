class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        ranks = sorted(score, reverse = True)

        ranking = {}
        for i, point in enumerate(ranks):
            if i == 0:
                ranking[point] = 'Gold Medal'
            elif i == 1:
                ranking[point] = 'Silver Medal'
            elif i == 2:
                ranking[point] = 'Bronze Medal'
            else:
                ranking[point] = str(i + 1)
        
        res = []
        for i in score:
            res.append(ranking[i])
        return res