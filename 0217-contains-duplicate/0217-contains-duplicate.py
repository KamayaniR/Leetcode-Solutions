class Solution(object):
    def containsDuplicate(self, nums):
        distinct_num = set(nums)
        return len(nums) != len(distinct_num)
        
        