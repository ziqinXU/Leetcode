class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        A=sorted(arr)
        mindiff=100000
        returnarray=[]
        for i in range(len(A)-1):
            if A[i+1]-A[i]<mindiff:
                mindiff=A[i+1]-A[i]
        for i in range(len(A)-1):
            if A[i+1]-A[i]==mindiff:
                returnarray.append([A[i],A[i+1]])
        return returnarray
            
