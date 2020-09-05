class Solution:
    def numSquares(self, n: int) -> int:
        dp=[float('NaN')]*(n+1)
        dp[0]=0
        numsquarelist=[x**2 for x in range(1,int(math.sqrt(n))+1)]
        #print(numsquarelist)
        for i in range(1,n+1):
            for squarenum in numsquarelist:
                if squarenum>i:
                    break
                dp[i]=min(dp[i-squarenum]+1,dp[i])#+1加上这个完全平方数
        #print(dp)
        return dp[-1]
