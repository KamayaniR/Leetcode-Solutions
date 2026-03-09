class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        result = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[result] = nums[i]
                result+=1
        return result