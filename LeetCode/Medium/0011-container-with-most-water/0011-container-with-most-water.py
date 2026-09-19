class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        most_water = 0

        while l <= r:
            width = r - l
            tall = min(height[l], height[r])
            most_water = max(most_water, width * tall)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return most_water