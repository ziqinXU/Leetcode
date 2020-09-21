class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #并查集
        def find(x,parent):
            x_root=x
            while parent[x_root]!=-1:
                x_root=parent[x_root]
            return x_root
        def union(x,y,parent,rank):
            x_root=find(x,parent)
            y_root=find(y,parent)
            if x_root==y_root:#形成环
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
        parent=[-1]*(len(edges)+1)
        rank=[0]*(len(edges)+1)
        returnarr=[]
        for i in range(len(edges)):
            if union(edges[i][0],edges[i][1],parent,rank)==0:
                returnarr.append(edges[i])
        return returnarr[-1]
