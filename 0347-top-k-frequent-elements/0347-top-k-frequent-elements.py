class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out = []
        bucket = [[]for i in range(len(nums)+1)]
        count = Counter(nums)

        for j,freq in count.items():
            bucket[freq].append(j)

        for i in range(len(bucket)-1,0,-1):
            for j in bucket[i]:
                out.append(j)
            if len(out) == k:
                return out        