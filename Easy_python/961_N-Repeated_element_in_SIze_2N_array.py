class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        diction={}
        for i in range(len(A)):
            diction[A[i]]=A.count(A[i])
            if A.count(A[i])==len(A)/2:
                return A[i]
