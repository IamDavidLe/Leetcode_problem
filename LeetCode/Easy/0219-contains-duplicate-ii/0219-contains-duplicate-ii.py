class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        visit = {}

        for i, val in enumerate(nums):
            if val in visit:
                if i - visit[val] <= k:
                    return True

            visit[val] = i

        return False