from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        blocks = deque()
        right = len(nums) - 1
        cost = 0
        answer = 0

        for left in range(len(nums) - 1, -1, -1):
            while blocks and nums[blocks[-1]] <= nums[left]:
                start = blocks.pop()
                end = blocks[-1] if blocks else right + 1
                cost += (nums[left] - nums[start]) * (end - start)

            blocks.append(left)

            while cost > k:
                block_start = blocks[0]
                cost -= nums[block_start] - nums[right]

                if block_start == right:
                    blocks.popleft()

                right -= 1

            answer += right - left + 1

        return answer