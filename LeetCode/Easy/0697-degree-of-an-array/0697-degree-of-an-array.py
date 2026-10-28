class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        degree = max(count.values())

        first = {}
        last = {}
        for i, val in enumerate(nums):
            if count[val] == degree :
                if val not in first:
                    first[val] = i
                
                last[val] = i
        
        smallest = float('inf')
        for num in first:
            smallest = min(smallest, last[num] - first[num] + 1)
        
        return smallest
                
         