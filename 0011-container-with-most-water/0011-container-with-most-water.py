class Solution(object):
    def maxArea(self, height):
        max_volume = 0
        right = len(height) - 1
        left = 0

        while left < right:
            width = right - left
            height1 = min(height[left], height[right])
            volume = width * height1

            max_volume = max(max_volume,volume)
            
            if height[left] < height[right]:
                left+=1
            else:
                right -=1

        return max_volume
        