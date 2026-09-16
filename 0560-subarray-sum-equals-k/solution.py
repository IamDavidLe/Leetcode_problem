class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        prefix_sum = {0 : 1}
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            last_piece = cur_sum - k
            if last_piece in prefix_sum:
                result += prefix_sum[last_piece]
            
            prefix_sum[cur_sum] = 1 + prefix_sum.get(cur_sum, 0)
        
        return result 