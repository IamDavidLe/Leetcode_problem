class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        count = {x:0 for x in nums}
        for n in nums:
            count[n] += 1
        
        def backtracking():
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1

                    backtracking()

                    count[n] += 1
                    perm.pop()
        
        backtracking()
        return res
