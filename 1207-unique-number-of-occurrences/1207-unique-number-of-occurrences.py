class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        occ = count.values()
        freq = set(occ)

        return len(freq) == len(occ)
        