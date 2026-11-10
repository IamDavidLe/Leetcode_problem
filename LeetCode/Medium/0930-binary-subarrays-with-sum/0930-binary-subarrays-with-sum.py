class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        prefix_sum = 0
        count = 0
        hashmap = {0: 1}

        for num in nums:
            prefix_sum += num
            val = prefix_sum - goal

            if val in hashmap:
                count += hashmap[val]

            hashmap[prefix_sum] = 1 + hashmap.get(prefix_sum, 0)

        return count