class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        A=str(bin(n))
        if A[2]=='1':
            for i in range(2,len(A),2):
                if A[i]!='1':
                    return False
            for i in range(3,len(A),2):
                if A[i]!='0':
                    return False
            return True
        if A[2]=='0':
            for i in range(2,len(A),2):
                if A[i]!='0':
                    return False
            for i in range(3,len(A),2):
                if A[i]!='1':
                    return False
            return True
