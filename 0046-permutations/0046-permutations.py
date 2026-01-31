class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(current, rem):
            if not rem:
                result.append(current[:])
                return
            for i in range(len(rem)):
                backtrack(current + [rem[i]],rem[:i] + rem[i+1:])
            
        backtrack([],nums)
        return result

        