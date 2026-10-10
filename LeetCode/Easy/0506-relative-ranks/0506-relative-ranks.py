class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        ranking = sorted(score[:], reverse = True)
        res = []
        for i in score:
            rank = ranking.index(i) + 1
            if rank == 1:
                res.append('Gold Medal')
            elif rank == 2:
                res.append('Silver Medal')
            elif rank == 3:
                res.append('Bronze Medal')
            else:
                res.append(f'{rank}')
        
        return res

