class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = 0
        for i in range(len(arr1)):
            increase = True
            for j in range(len(arr2)):
                val = abs(arr1[i] - arr2[j])
                if val <= d:
                    increase = False
                    break
                
            if increase:
                count += 1
        
        return count