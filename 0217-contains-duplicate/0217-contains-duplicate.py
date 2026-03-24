class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        frequency = Counter(nums)
        count = frequency.values()
        for i in count:
            if i>=2:
                return True
        return False
      
        