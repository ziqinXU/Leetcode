class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i=0
        S=list(S)
        while i <len(S):
            if S[i]=='#' and i-1>=0:
                del S[i],S[i-1]
                i=i-2
            
            elif S[i]=='#' and i==0:
                del S[i]
                i=i-1
            i=i+1
        T=list(T)
        i=0
        while i <len(T):
            if T[i]=='#' and i-1>=0:
                del T[i],T[i-1]
                i=i-2

            elif T[i]=='#' and i==0:
                del T[i]
                i=i-1
            i=i+1      
        if S==T:
            return True
        else:
            return False
