class Solution:
    def reverseBits(self, n: int) -> int:
        A=str(bin(n))[2:]
        A=A.zfill(32)
        B=""
        for i in reversed(range(len(A))):
            B=B+A[i]
        return int(B,2)
        
