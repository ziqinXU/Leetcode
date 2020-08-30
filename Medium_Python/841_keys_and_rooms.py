#典型dfs题目，用数组记录已经拜访过的房间
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=[0]*len(rooms)
        def dfs(visited,rooms,cur):
            stack=[]
            seen=set()
            seen.add(cur)
            stack.append(cur)
            while(len(stack)>0):
                cur=stack.pop()
                visited[cur]=1
                nodes=rooms[cur]
                for w in nodes:
                    if w not in seen:
                        seen.add(w)
                        stack.append(w)
        dfs(visited,rooms,0)
        if 0 in visited:
            return False
        else:
            return True
