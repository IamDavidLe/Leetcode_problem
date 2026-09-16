class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        l = 0
        count = {}
        for r in range(k, len(nums)+1):
            for num in set(nums[l:r]):
                count[num] = 1 + count.get(num, 0)
            l += 1
        
        largest = []
        for num in set(nums):
            if count[num] == 1:
                largest.append(num)

        if largest:
            return max(largest)
        return -1