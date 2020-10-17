class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #无橘子/无腐烂橘子/无好橘子
        #注意同时开始腐烂的条件,一次性加入所有烂橘子开始搜索，一共搜索深度即为所需结果
        def bfs(grid,visited,queue,i,j):
            depth=-1
            directions=[[0,1],[0,-1],[1,0],[-1,0]]
            while (len(queue)>0):
                size=len(queue)
                depth+=1
                while(size>0):
                    
                    cur=queue.pop(0)
                   
                    flag=0
                    for pos in directions:
                        newi=cur[0]
                        newj=cur[1]
                        newi+=pos[0]
                        newj+=pos[1]
                        if 0<=newi and newi<len(grid) and 0<=newj and newj<len(grid[0]) and grid[newi][newj]==1 and visited[newi][newj]==0:
                            flag=1
                            visited[newi][newj]=1
                            queue.append([newi,newj])
                    
                    size-=1
                
            return depth
        totaldepth=0
        goodlist=[]
        queue=[]

        visited=[[0]*len(grid[0]) for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    queue.append([i,j])
                    visited[i][j]=1
                if grid[i][j]==1:
                    goodlist.append([i,j])
        if len(queue)==0 and len(goodlist)==0:
            return 0
        if len(queue)!=0:
            depth=bfs(grid,visited,queue,queue[0][0],queue[0][1])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and visited[i][j]==0:
                    return -1
        return depth
