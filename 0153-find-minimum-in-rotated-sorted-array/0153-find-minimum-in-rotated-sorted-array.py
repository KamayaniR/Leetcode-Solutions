class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = nums.sort()
        return nums[0]