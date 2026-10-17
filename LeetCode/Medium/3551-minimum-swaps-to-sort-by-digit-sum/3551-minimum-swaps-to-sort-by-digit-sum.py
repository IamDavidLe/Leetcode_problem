class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        target = []
        pairs = []
        for num in nums:
            count = 0
            original = num
            while num > 0:
                count += num % 10
                num //= 10
            
            pairs.append((count, original))
        
        pairs.sort()
        for digit_sum, switch in pairs:
            target.append(switch)
        
        location = {num : i for i, num in enumerate(nums)}
        swap = 0
        for i in range(len(nums)):
            if nums[i] != target[i]:
                j = location[target[i]]

                location[nums[i]] = j
                location[nums[j]] = i
                nums[i], nums[j] = nums[j], nums[i]

                swap += 1
        
        return swap