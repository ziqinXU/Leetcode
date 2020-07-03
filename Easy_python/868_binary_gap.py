class Solution:
    def binaryGap(self, N: int) -> int:
        maxlen=0
        A=str(bin(N))[2:]
        pos=[]
        for i in range(len(A)):
            if A[i]=='1':
                pos.append(i)
        for i in range(len(pos)-1):
            if pos[i+1]-pos[i]>maxlen:
                maxlen=pos[i+1]-pos[i]
        return maxlen
