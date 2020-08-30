#从顶部看，由该形状生成的阴影将是网格中非零值的数目。
#从侧面看，由该形状生成的阴影将是网格中每一行的最大值。
#从前面看，由该形状生成的阴影将是网格中每一列的最大值。---官方

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        arrsum=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]>0:
                    arrsum += 1
        for i in range(len(grid)):
            arrsum=arrsum+max(grid[i])
        for j in range(len(grid)):
            A=[row[j] for row in grid]
            arrsum=arrsum+max(A)

        return arrsum
