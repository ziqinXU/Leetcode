class Solution:
    def bitwiseComplement(self, N: int) -> int:
        A=str(bin(N))[2:]
        A=list(A)
        for i in range(len(A)):
            if A[i]=='0':
                A[i]='1'
            else:
                A[i]='0'
        return int("".join(A),2)
