class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        A=sorted(stones)
        while len(A)!=1:
            new=A[len(A)-1]-A[len(A)-2]        
            del A[len(A)-1]
            del A[len(A)-1]
            A.append(new)
            A=sorted(A)
        return A[0]
