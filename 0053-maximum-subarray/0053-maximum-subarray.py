class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = max_sum = nums[0]
        for num in nums[1:]:
            curr_sum = max(num, num + curr_sum)
            max_sum = max(curr_sum, max_sum)
        return max_sum
        