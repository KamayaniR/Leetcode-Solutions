class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return sorted(count, key=count.get,reverse = True)[:k]

        