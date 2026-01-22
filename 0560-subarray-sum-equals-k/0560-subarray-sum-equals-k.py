class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sums = 0
        prefix_counts ={0:1}
        
        for i in nums:
            sums+=i
            if sums - k in prefix_counts:
                count+= prefix_counts[sums-k]
            prefix_counts[sums]= prefix_counts. get(sums,0)+1
        return count