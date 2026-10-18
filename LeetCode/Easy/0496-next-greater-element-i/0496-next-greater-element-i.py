class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        for i in range(len(nums1)):
            j = nums2.index(nums1[i])
            while j < len(nums2) and nums2[j] <= nums1[i]:
                j += 1 
            
            if j < len(nums2):
                res.append(nums2[j])
            else:
                res.append(-1)
        
        return res