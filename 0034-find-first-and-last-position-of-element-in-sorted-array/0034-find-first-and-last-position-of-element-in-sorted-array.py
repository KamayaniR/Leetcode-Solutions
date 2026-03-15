class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if nums and nums[0] <= target <= nums[~0]:
            left, right = bisect_left(nums,target), bisect_right(nums,target)
            
            if left < right:
                 return[left, right-1]
        return [-1,-1]
        


         
        