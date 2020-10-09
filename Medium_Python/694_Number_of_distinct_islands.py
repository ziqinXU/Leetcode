class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        visited=[[0]*len(grid[0]) for i in range(len(grid))]
        def dfs(grid,visited,i,j,lefti,leftj,seen):
            nodes=[[i+1,j],[i,j+1],[i-1,j],[i,j-1]]
            for k in nodes:
                if k[0]>=0 and k[0]<len(grid) and k[1]>=0 and k[1]<len(grid[0]) and grid[k[0]][k[1]]==1 and visited[k[0]][k[1]]==0:
                    seen.append((k[0]-lefti,k[1]-leftj))
                    visited[k[0]][k[1]]=1
                    dfs(grid,visited,k[0],k[1],lefti,leftj,seen)
            return seen
        res=set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if visited[i][j]==0 and grid[i][j]==1:
                    
                    lefti,leftj=i,j
                    seen=[]
                    seen=dfs(grid,visited,i,j,lefti,leftj,seen)
                    res.add(tuple(seen))#用tuple将list转换
        return len(res)
                    
