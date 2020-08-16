#标记方向及走过的路程
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix)==0:
            return []
        res = []
        x=0
        y=0
        i = 1
        direction=0
        m=len(matrix)
        n=len(matrix[0])
        while i <= m*n:
            i=i+1
            if direction==0:
                res.append(matrix[x][y])
                matrix[x][y]=0
                y=y+1
                if y>=n or matrix[x][y]==0:
                    direction=1
                    y=y-1
                    x=x+1
                continue
            if direction==1:
                res.append(matrix[x][y])
                matrix[x][y]=0
                x=x+1
                if x>=m or matrix[x][y]==0:
                    x=x-1
                    y=y-1
                    direction=2
                continue
            if direction==2:
                res.append(matrix[x][y])
                matrix[x][y]=0
                y=y-1
                if y<0 or matrix[x][y]==0:
                    y=y+1
                    x=x-1
                    direction=3
                    
                continue
            if direction==3:
                res.append(matrix[x][y])
                matrix[x][y]=0
                x=x-1
                if x<0 or matrix[x][y]==0:
                    x=x+1
                    y=y+1
                    direction=0
                continue

        return res
                     
