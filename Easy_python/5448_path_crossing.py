class Solution:
    def isPathCrossing(self, path: str) -> bool:
        pos=[(0,0)]
        x=0
        y=0
        for i in range(len(path)):
            if path[i]=='N':
                x=x
                y=y+1
            if path[i]=='E':
                x=x+1
                y=y
            if path[i]=='W':
                x=x-1
                y=y
            if path[i]=='S':
                x=x
                y=y-1
            current=(x,y)

            if current in pos:
                return True
            pos.append(current)
        return False
            
            

        
