class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        even = 1  # Prefix with empty value --> 0
        odd = 0
        prefix_sum = 0
        count = 0

        for num in arr:
            prefix_sum += num

            if prefix_sum % 2 == 0:
                count += odd
                even += 1
            else:
                count += even
                odd += 1

        return count % (10**9 + 7)