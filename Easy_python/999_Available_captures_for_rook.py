class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        
        for i in range(len(board)):
            if 'R' in board[i]:
                pos=[i,board[i].index('R')]
        x=pos[0]
        y=pos[1]
        count=0
        while x>=0:
            if board[x][y]=='B':
                break
            if board[x][y]=='p':
                count=count+1
                break
            x=x-1
        x=pos[0]
        y=pos[1]
        while x<len(board):
            if board[x][y]=='B':
                break
            if board[x][y]=='p':
                count=count+1
                break
            x=x+1
        x=pos[0]
        y=pos[1]
        while y>=0:
            if board[x][y]=='B':
                break
            if board[x][y]=='p':
                count=count+1
                break
            y=y-1
        x=pos[0]
        y=pos[1]
        while y<len(board[0]):
            if board[x][y]=='B':
                break
            if board[x][y]=='p':
                count=count+1
                break
            y=y+1
        return count
        
