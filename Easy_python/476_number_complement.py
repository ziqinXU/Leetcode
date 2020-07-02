class Solution:
    def findComplement(self, num: int) -> int:
        A=list(str(bin(num)))
        #print(A)
        for i in range(2,len(A)):
            if A[i]=='0':
                A[i]='1'
            else:
                A[i]='0'

        return int("".join(A[2:]),2)
