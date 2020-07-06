class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A)==0:
            return False
        if A.index(max(A))==0 or A.index(max(A))==len(A)-1:
            return False
        else:
            peak=A.index(max(A))
            for i in range(peak):
                if A[i]>=A[i+1]:
                    return False
            for i in range(peak,len(A)-1):
                if A[i]<=A[i+1]:
                    return False
            return True
