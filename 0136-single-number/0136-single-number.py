class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        singleNum = 0;
        for i in nums:
            singleNum ^=i;
        return singleNum
        