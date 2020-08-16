class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix=[[0]*n for i in range(n)]
        if n==0:
            return []
        x=0
        y=0
        i = 0
        direction=0
        m=n
        while i < n*n:
            i=i+1
            if direction==0:
                matrix[x][y]=i
                y=y+1
                if y>=n or matrix[x][y]!=0:
                    direction=1
                    y=y-1
                    x=x+1
                continue
            if direction==1:
                matrix[x][y]=i
                x=x+1
                if x>=m or matrix[x][y]!=0:
                    x=x-1
                    y=y-1
                    direction=2
                continue
            if direction==2:
                matrix[x][y]=i
                y=y-1
                if y<0 or matrix[x][y]!=0:
                    y=y+1
                    x=x-1
                    direction=3
                continue
            if direction==3:
                matrix[x][y]=i
                x=x-1
                if x<0 or matrix[x][y]!=0:
                    x=x+1
                    y=y+1
                    direction=0
                continue

        return matrix
                     
        
