class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num = set(nums)
        return len(nums)!= len(num)
      
        