class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)<=1:
            return 0
        max_diff = 0
        for i in range(len(nums)-1):
            p1= i
            p2=i+1
            diff = abs(nums[p1] - nums[p2])
            max_diff = max(diff,max_diff)

        return max_diff
            

        