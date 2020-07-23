class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A=sorted(A)
        i=len(A)-3
        while i>=0:
            if A[i]+A[i+1]>A[i+2]:
                return A[i]+A[i+1]+A[i+2]
            i=i-1
        return 0
