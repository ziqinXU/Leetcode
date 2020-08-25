#典型dfs题，走过的路可以记为0
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j,grid):
            stack=[]
            stack.append((i,j))
            #print(i,j)
            seen=set()
            seen.add((i,j))
            while len(stack)>0:
                (ic,jc)=stack.pop()
                if ic-1>=0 and grid[ic-1][jc]==1:
                    if (ic-1,jc) not in seen:
                        stack.append((ic-1,jc))
                        seen.add((ic-1,jc))
                        grid[ic-1][jc]=0
                if jc-1>=0 and grid[ic][jc-1]==1:
                    if (ic,jc-1) not in seen:
                        stack.append((ic,jc-1))
                        seen.add((ic,jc-1))
                        grid[ic][jc-1]=0
                if ic+1<len(grid) and grid[ic+1][jc]==1:
                    if (ic+1,jc) not in seen:
                        stack.append((ic+1,jc))
                        seen.add((ic+1,jc))
                        grid[ic+1][jc]=0
                if jc+1<len(grid[0]) and grid[ic][jc+1]==1:
                    if (ic,jc+1) not in seen:
                        stack.append((ic,jc+1))
                        seen.add((ic,jc+1))
                        grid[ic][jc+1]=0
            return grid,seen
        returncount=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    grid,seen=dfs(i,j,grid)
                    #print(seen)
                    count=len(seen)
                    if count>returncount:
                        returncount=count
        return returncount
