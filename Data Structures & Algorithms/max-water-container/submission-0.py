class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        width = 0
        left = 0
        right = len(heights)-1
        while(left < right):
            minHight = min(heights[left],heights[right])
            width = right - left
            water = width * minHight
            maxWater = max(water,maxWater)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxWater