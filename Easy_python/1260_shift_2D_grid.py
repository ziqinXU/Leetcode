class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if k==0:
            return grid
        returnlist=[[0]*len(grid[0]) for i in range(len(grid))]
        temparr=[]
        k=k%(len(grid[0])*len(grid))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                temparr.append(grid[i][j])
        temparr=temparr[-k:]+temparr[:-k]
        t=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                returnlist[i][j]=temparr[t]
                t=t+1
        return returnlist
