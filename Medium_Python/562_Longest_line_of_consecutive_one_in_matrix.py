class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        #4dps
        dp1=[[0]*len(M[0]) for i in range(len(M))]#hori
        dp2=[[0]*len(M[0]) for i in range(len(M))]#ver
        dp3=[[0]*len(M[0]) for i in range(len(M))]#diag
        dp4=[[0]*len(M[0]) for i in range(len(M))]#anti-diag
        maxval=0
        if len(M)==0:
            return 0
        for i in range(len(M)):
            dp1[i][0]=M[i][0]
            dp3[i][0]=M[i][0]
            dp4[i][len(M[0])-1]=M[i][len(M[0])-1]
            if dp1[i][0]>maxval:
                maxval=dp1[i][0]
            if M[i][len(M[0])-1]>maxval:
                maxval=M[i][len(M[0])-1]
        for j in range(len(M[0])):
            dp2[0][j]=M[0][j]
            dp3[0][j]=M[0][j]
            dp4[0][j]=M[0][j]
            if M[0][j]>maxval:
                maxval=M[0][j]
        for i in range(len(M)):
            for j in range(1,len(M[0])):
                if M[i][j]==1:
                    dp1[i][j]=dp1[i][j-1]+1
                    if dp1[i][j]>maxval:
                        maxval=dp1[i][j]
                else:
                    dp1[i][j]=0
        for i in range(1,len(M)):
            for j in range(len(M[0])):
                if M[i][j]==1:
                    dp2[i][j]=dp2[i-1][j]+1
                    if dp2[i][j]>maxval:
                        maxval=dp2[i][j]
                else:
                    dp2[i][j]=0
        
        for i in range(1,len(M)):
            for j in range(1,len(M[0])):
                if M[i][j]==1:
                    dp3[i][j]=dp3[i-1][j-1]+1
                    if dp3[i][j]>maxval:
                        maxval=dp3[i][j]
                else:
                    dp3[i][j]=0
        
        for i in range(1,len(M)):
            for j in reversed(range(len(M[0])-1)):
                if M[i][j]==1:
                    #print(i,j)
                    dp4[i][j]=dp4[i-1][j+1]+1
                    if dp4[i][j]>maxval:
                        maxval=dp4[i][j]
                else:
                    dp4[i][j]=0
        #print(dp4)
        return maxval
        
