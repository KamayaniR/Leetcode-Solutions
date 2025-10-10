class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for i in strs:
            out = tuple(sorted(i))
            result[out].append(i)
        return list(result.values())
