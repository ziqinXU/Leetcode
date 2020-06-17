class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        for idx in range(len(A)):
            if idx+1<len(A):
                if A[idx]>A[idx+1] and A[idx]>A[idx-1]:
                    return idx
        return idx
