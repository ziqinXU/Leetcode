class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        A=A+A
        if A.find(B)!=-1 and len(A)==2*len(B):
            return True
        else:
            return False
