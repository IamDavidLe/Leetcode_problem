class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        res = []
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue

            else:
                k += 1
                res.append(nums[i])
        
        nums[:] = res
        return k