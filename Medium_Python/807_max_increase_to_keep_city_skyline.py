class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rowmax=[max(row) for row in grid]
        colmax=[max(col) for col in zip(*grid)]
        arrsum=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                arrsum+=min(rowmax[r],colmax[c])-grid[r][c]
        return arrsum
