class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        def bfs(matrix,i,j):
            queue=[]
            seen=set()
            queue.append([i,j])
            seen.add((i,j))
            depth=1
            
            while(len(queue)>0):    
                size = len(queue)
                while (size!=0):
                    size-=1
                    node=queue.pop(0)
                    i,j=node[0],node[1]
                    nodes=[[i+1,j],[i,j+1],[i-1,j],[i,j-1]]
                    for k in nodes:
                        if k[0]>=0 and k[0]<len(matrix) and k[1]>=0 and k[1]<len(matrix[0]) and matrix[k[0]][k[1]]==0:
                            
                            return depth

                        if k[0]>=0 and k[0]<len(matrix) and k[1]>=0 and k[1]<len(matrix[0]) and (k[0],k[1]) not in seen:
                            seen.add((k[0],k[1]))
                            queue.append(k)
                        
                depth+=1      
            
        res=[[0]*len(matrix[0]) for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==1:
                    depth=bfs(matrix,i,j)
                    res[i][j]=depth
        return res
