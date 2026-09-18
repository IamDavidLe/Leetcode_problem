class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        pos = {}

        for i, c in enumerate(s):
            if c not in pos:
                pos[c] = [i, i]
            else:
                pos[c][1] = i

        def get_interval(left):
            right = pos[s[left]][1]
            i = left

            while i <= right:
                c = s[i]
                if pos[c][0] < left:
                    return None

                right = max(right, pos[c][1])
                i += 1

            return [left, right]

        intervals = []

        for i, c in enumerate(s):
            if i == pos[c][0]:
                interval = get_interval(i)

                if interval is not None:
                    intervals.append(interval)

        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1

        for left, right in intervals:
            if left > prev_end:
                result.append(s[left:right + 1])
                prev_end = right

        return result