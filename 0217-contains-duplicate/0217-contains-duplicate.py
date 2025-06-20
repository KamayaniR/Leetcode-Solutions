class Solution(object):
    def containsDuplicate(self, nums):
        appear = Counter(nums)
        count = appear.values()
        for i in count:
            if i >= 2:
                return True
        return False

        
        