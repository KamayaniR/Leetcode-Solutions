class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        def backtrack(target,arr,start):
            if target == 0:
                res.append(list(arr))
            elif target < 0:
                return
            
            for i in range(start, len(candidates)):
                arr.append(candidates[i])
                backtrack(target-candidates[i],arr,i)
                arr.pop()
        backtrack(target,[],0)
        return res
        
        