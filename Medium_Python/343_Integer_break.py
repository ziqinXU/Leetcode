#类似剪绳子问题
class Solution:
    def integerBreak(self, n: int) -> int:
        #dp保存当前情况下可达到的最大乘积
        if n==2:
            return 1
        if n==3:
            return 2
        dp=[1]*(n+1) 
        dp[1]=1
        dp[2]=2
        dp[3]=3
        for i in range(4,n+1):
            maxval=-1
            for j in range(1,i//2+1):
                maxval=max(maxval,dp[j]*dp[i-j])
            dp[i]=maxval
            #print(dp[i])
        return dp[-1]

