class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_volume = 0

        while l < r:
            w = r - l
            h = min(height[r], height[l])

            volume = w*h
            max_volume = max(max_volume, volume)

            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return max_volume
        