class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        returnstring=""
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        d = dict( (word,(x, y)) for x, alphabet in enumerate(board) for y, word in enumerate(alphabet) )
        xlast=0
        ylast=0
        for i in range(len(target)):
            (x,y)=d[target[i]]
            if x-xlast>=0:
                actionx='D'
            else:
                actionx='U'
            if y-ylast>=0:
                actiony='R'
            else:
                actiony='L'
            if i-1>=0 and target[i-1]=='z':
                returnstring=returnstring+actionx*abs(x-xlast)+actiony*abs(y-ylast)+'!'
            elif target[i]=='z':
                returnstring=returnstring+actiony*abs(y-ylast)+actionx*abs(x-xlast)+'!'
            else:
                returnstring=returnstring+actionx*abs(x-xlast)+actiony*abs(y-ylast)+'!'
            
            xlast=x
            ylast=y
        return returnstring
