class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        diff=int((sum(A)-sum(B))/2)
        for i in range(len(A)):
            if A[i]-diff in B:
                return [A[i],A[i]-diff]
