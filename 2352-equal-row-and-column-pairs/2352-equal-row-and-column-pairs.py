class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_count = Counter(tuple(row) for row in grid)
  
        out = 0
        for i in range(n):
            col = tuple(grid[r][i] for r in range(n))
    
            out+=row_count[col]

        return out
