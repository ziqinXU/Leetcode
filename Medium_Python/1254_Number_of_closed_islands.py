class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if len(grid)==0:
            return 0
        visited=[[0]*len(grid[0]) for i in range(len(grid))]
        def dfs(grid,visited,i,j):
                if i-1>=0 and grid[i-1][j]==0 and visited[i-1][j]==0:
                    visited[i-1][j]=1
                    if i-1==0:
                        self.judge=1
                    dfs(grid,visited,i-1,j)
                if j-1>=0 and grid[i][j-1]==0 and visited[i][j-1]==0:
                    if j-1==0:
                        self.judge=1
                    visited[i][j-1]=1
                    dfs(grid,visited,i,j-1)
                if j+1<len(grid[0]) and grid[i][j+1]==0 and visited[i][j+1]==0:
                    visited[i][j+1]=1
                    if j+1==len(grid[0])-1:
                        self.judge=1
                    dfs(grid,visited,i,j+1)
                if i+1<len(grid) and grid[i+1][j]==0 and visited[i+1][j]==0:
                    visited[i+1][j]=1
                    if i+1==len(grid)-1:
                        self.judge=1
                    dfs(grid,visited,i+1,j)
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    if visited[i][j]==0:
                        if (i>0 and i<len(grid)-1 and j>0 and j<len(grid[0])-1):
                            visited[i][j]=1
                            self.judge=0
                            dfs(grid,visited,i,j)
                            if i==0 or j==0 or i==len(grid)-1 or j==len(grid[0])-1:
                                self.judge=1
                            
                            if self.judge!=1:
                                
                                count+=1
                        
        return count
