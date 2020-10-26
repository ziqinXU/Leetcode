class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        #每一行开头必须是1，每一列如果0个数大于1个数，则翻转
        for i in range(len(A)):
            if A[i][0]==0:
                for j in range(len(A[0])):
                    A[i][j]=1-A[i][j]
        
        
        for j in range(1,len(A[0])):
            count1,count0=0,0
            for i in range(len(A)):
                if A[i][j]==0:
                    count0+=1
                else:
                    count1+=1
            
            if count0>count1:
                for i in range(len(A)):
                    A[i][j]=1-A[i][j]
        res=0
        for i in range(len(A)):
            
            res+=int(''.join(map(str,A[i])),2)
        return res
