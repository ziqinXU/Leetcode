#dfs
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited=[0]*len(arr)
        stack=[start]

        visited[start]=-1
        while(len(stack)>0):
            node=stack.pop()
            nodes=[node-arr[node],node+arr[node]]
            for i in nodes:
                if i>=0 and i<len(arr) and arr[i]==0:
                    return True
                if i>=0 and i<len(arr) and visited[i]!=-1:
                    stack.append(i)
                    visited[i]=-1

        return False
