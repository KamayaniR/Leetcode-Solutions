class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for i in range (len(nums)):
            dict[nums[i]]= i
        
        for i in range(len(nums)):
            comp = target - nums[i]
        
            if comp in dict and dict[comp] != i :
                return dict[comp],i