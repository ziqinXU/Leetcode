class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=[[0]*len(grid[0]) for i in range(len(grid))]

        def dfs(grid,visited,i,j):
            if i-1>=0 and grid[i-1][j]=='1' and visited[i-1][j]==0:
                visited[i-1][j]=1
                dfs(grid,visited,i-1,j)
            if j-1>=0 and grid[i][j-1]=='1' and visited[i][j-1]==0:
                visited[i][j-1]=1
                dfs(grid,visited,i,j-1)
            if j+1<len(grid[0]) and grid[i][j+1]=='1' and visited[i][j+1]==0:
                visited[i][j+1]=1
                dfs(grid,visited,i,j+1)
            if i+1<len(grid) and grid[i+1][j]=='1'and visited[i+1][j]==0:
                visited[i+1][j]=1
                dfs(grid,visited,i+1,j)
            return visited
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j]==0 and grid[i][j]=='1':
                    #start=[i,j]
                    visited[i][j]=1
                    visited = dfs(grid,visited,i,j)
                    #print(visited)
                    count=count+1
                    
        return count
