class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        out = []

        for i in range(len(candies)):
            if candies[i]+extraCandies >= max(candies):
                out.append(True)
            else:
                out.append(False)
        
        return out
        