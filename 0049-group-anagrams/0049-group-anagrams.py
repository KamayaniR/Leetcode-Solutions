class Solution(object):
    def groupAnagrams(self, strs):
        result = defaultdict(list)

        for i in strs:
            output = tuple(sorted(i))
            result[output].append(i)
        return result.values()

        