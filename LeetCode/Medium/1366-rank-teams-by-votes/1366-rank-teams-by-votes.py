class Solution:
    def rankTeams(self, votes: list[str]) -> str:
        n = len(votes[0])
        count = {c: [0] * n for c in votes[0]}

        for teams in votes:
            for rank, team in enumerate(teams):
                count[team][rank] += 1
        
        final = sorted(count, key = lambda c: ([-x for x in count[c]], c)) 
        # Compare the number of votes first, if all of them are equal, then compare two teams by alphabet order

        return ''.join(final)