class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #动态规划，找出左上，上，左中最小值+1
        if len(matrix)==0:
            return 0
        dp=[[0]*len(matrix[0]) for i in range(len(matrix))]
        maxdp=0
        for i in range(len(matrix)):
            if matrix[i][0]=="1":
                dp[i][0]=1
                maxdp=1
        for j in range(len(matrix[0])):
            if matrix[0][j]=="1":
                dp[0][j]=1
                maxdp=1
        #print(dp)
        
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j]=="1":
                    #print(i,j)
                    #print(dp[i-1][j])
                    dp[i][j]=min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1
                    if dp[i][j]>maxdp:
                        maxdp=dp[i][j]
        
        return maxdp**2
