class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, 1
        seen = set()
        count = 0
        while r < len(nums):
            val = nums[r] - nums[l]
            if val == k:
                if nums[l] not in seen:
                    count += 1
                    seen.add(nums[l])
                l += 1
                r += 1
            elif val < k:
                r += 1
            else:
                l += 1
                if l == r:
                    r+=1
        
        return count
                