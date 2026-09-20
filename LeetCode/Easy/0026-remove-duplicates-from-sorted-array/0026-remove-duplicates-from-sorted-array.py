class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = 0
        k = 1
        res = [nums[0]]
        for r in range(1, len(nums)):
            if nums[r] == nums[l]:
                continue
            
            else:
                res.append(nums[r])
                k += 1
                l = r
        nums[:] = res  # change all the elements in nums
        return k
