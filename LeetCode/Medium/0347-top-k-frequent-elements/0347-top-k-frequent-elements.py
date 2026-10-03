class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for val, time in count.items():
            freq[time].append(val)
        
        res = []
        for i in range(len(nums), 0, -1): # stop at index 1 because we don't have to check freq[0]
            if freq[i]:
                res.extend(freq[i])
                if len(res) == k:
                    return res