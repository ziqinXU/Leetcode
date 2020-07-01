class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x=0
        y=0
        for i in range(len(moves)):
            if moves[i]=='U':
                x=x
                y=y+1
            if moves[i]=='D':
                x=x
                y=y-1
            if moves[i]=='R':
                x=x+1
                y=y
            if moves[i]=='L':
                x=x-1
                y=y
        if x==0 and y==0:
            return True
        else:
            return False
