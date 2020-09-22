class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        connections.sort(key=lambda edges:edges[2])
        parent=[-1]*(N+1)
        def find(x,parent):
            x_root=x
            
            while(parent[x_root]!=-1):
                x_root=parent[x_root]
            return x_root
        def union(x,y,parent,rank):
            x_root=find(x,parent)
            y_root=find(y,parent)
            if x_root==y_root:
                return 0
            else:
                if rank[x]>rank[y]:
                    parent[y_root]=x_root
                elif rank[x]<rank[y]:
                    parent[x_root]=y_root
                else:
                    parent[x_root]=y_root
                    rank[y_root]+=1
                return 1

        rank=[0]*(N+1)
        totalcost=0
        cnt=0
        for i in range(len(connections)):
            result=union(connections[i][0],connections[i][1],parent,rank)
            if result==1:
                
                totalcost+=connections[i][2]
                cnt+=1
            
        if cnt==N-1:
            return totalcost
        else:
            return -1
