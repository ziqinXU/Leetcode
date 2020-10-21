class Solution:
    def earliestAcq(self, logs: List[List[int]], N: int) -> int:
        logs.sort(key=lambda k:k[0])#先按时间排序
        parent=[-1]*N
        rank=[0]*N
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

                if rank[x_root]>rank[y_root]:
                    parent[y_root]=x_root
                elif rank[x_root]<rank[y_root]:
                    parent[x_root]=y_root
                else:
                    parent[x_root]=y_root
                    rank[x_root]+=1
                return 1
        for i in range(len(logs)):
            union(logs[i][1],logs[i][2],parent,rank)
            if parent.count(-1)==1:
                return logs[i][0]
        return -1
