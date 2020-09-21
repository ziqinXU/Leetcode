#并查集
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def find(x,parent):
            x_root=x
            while parent[x_root]!=-1:
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
        parent=[-1]*n
        rank=[0]*n
        for i in range(len(edges)):
            returnval=union(edges[i][0],edges[i][1],parent,rank)
        #print(parent)
        return parent.count(-1)
        
