class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counts = {}
        operations = 0
        for i in nums:
            need = k - i

            if counts.get(need,0) > 0:
                operations +=1
                counts[need] -=1
            else:
                counts[i] = counts.get(i,0) + 1
        return operations

        