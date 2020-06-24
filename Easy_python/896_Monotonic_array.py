class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        B=sorted(A)
        C=sorted(A,reverse=True)
        if A==B or C==A:
            return True
        return False
