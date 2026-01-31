class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        curr = []

        def Backtrack(start):
            if len(curr) ==k:
                result.append(curr[:])
                return

            for i in range(start,n+1):
                curr.append(i)
                Backtrack(i+1)
                curr.pop()

        Backtrack(1)
        return result
        