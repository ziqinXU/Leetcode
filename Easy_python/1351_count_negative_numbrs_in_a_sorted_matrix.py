class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for i in range(len(grid)):
            for j in reversed(range(len(grid[0]))):
                if grid[i][j]<0:
                    count=count+1
                if grid[i][j]>=0:
                    break
        return count
