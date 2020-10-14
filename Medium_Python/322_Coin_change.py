class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        dp=[10000000]*(amount+1)
        dp[0]=0
        for i in range(amount+1):
            for j in range(len(coins)):
                if i-coins[j]>=0:
                    dp[i]=min(dp[i],dp[i-coins[j]]+1)
        if dp[-1]!=10000000:
            return dp[-1]
        else:
            return -1
