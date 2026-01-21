class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0

        for i in range(len(nums)):
            if nums[i]!=0:
                nums[write],nums[i] = nums[i],nums[write]
                write+=1
        