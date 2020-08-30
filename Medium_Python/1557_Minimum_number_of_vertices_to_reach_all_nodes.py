class Solution:
#只需要找入度为0的点
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        visited=[0]*n
        for i in range(len(edges)):
            visited[edges[i][1]]+=1
        res=[]
        for i in range(len(visited)):
            if visited[i]==0:
                res.append(i)
        return res
