class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        count=0
        for j in range(len(A[0])):
            array=""
            for i in range(len(A)):
                array=array+A[i][j]
            if list(array)!=sorted(array):
                count=count+1

        return count
