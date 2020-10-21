class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i,j=0,0#i,j相同则加，否则判断j和前一位是否相同
        while j<len(typed):
            if i<len(name) and typed[j]==name[i]:    
                i+=1
                j+=1
            elif j>0 and typed[j-1]==typed[j]:
                j=j+1
            else:
                return False

        if i!=len(name):
            return False
        return True
