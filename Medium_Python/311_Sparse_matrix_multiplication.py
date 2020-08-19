class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        returnmatrix=[[0]*len(B[0]) for i in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                elementsum=0
                for k in range(len(A[0])):
                    elementsum=elementsum+A[i][k]*B[k][j]
                returnmatrix[i][j]=elementsum
        return returnmatrix
