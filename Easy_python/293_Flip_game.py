class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        returnarray=[]
        for idx,plus in enumerate(s):
            if idx<len(s)-1:
                if s[idx]=='+' and s[idx+1]=='+':
                    new_liststring=list(s)
                    new_liststring[idx]="-"
                    new_liststring[idx+1]="-"
                    tempstring="".join(new_liststring)
                    returnarray.append(tempstring)
        return returnarray
