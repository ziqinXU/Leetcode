#特殊性，只需要计算从0至N-1路径
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res=[]
        def dfs(graph,templist,res,start):
            if start==len(graph)-1:
                #print(templist)
                res.append(templist)
            for nodes in graph[start]:
                dfs(graph,templist+[nodes],res,nodes)
        dfs(graph,[0],res,0)
        return res




        
