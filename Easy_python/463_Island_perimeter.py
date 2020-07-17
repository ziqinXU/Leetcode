class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        lensum=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                tempcount=0
                if grid[i][j]==1:
                    if i-1>=0 and grid[i-1][j]==1:
                        tempcount=tempcount+1
                    if i+1<len(grid) and grid[i+1][j]==1:
                        tempcount=tempcount+1
                    if j+1<len(grid[0]) and grid[i][j+1]==1:
                        tempcount=tempcount+1
                    if j-1>=0 and grid[i][j-1]==1:
                        tempcount=tempcount+1
                    if tempcount==4:
                        lensum=lensum+0
                    elif tempcount==2:
                        lensum=lensum+2
                    elif tempcount==1:
                        lensum=lensum+3
                    elif tempcount==3:
                        lensum=lensum+1
                    else:
                        lensum=lensum+4
        return lensum

