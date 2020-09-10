class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        #记录当前cost+其他两种颜色在上一个房子时dp的最小值为当前的dp值
        dp=[[0]*3 for i in range(len(costs))]
        if len(costs)==0:
            return 0
        dp[0][0]=costs[0][0]
        dp[0][1]=costs[0][1]
        dp[0][2]=costs[0][2]
        for i in range(1,len(costs)):
            dp[i][0]=min(dp[i-1][1],dp[i-1][2])+costs[i][0]
            dp[i][1]=min(dp[i-1][0],dp[i-1][2])+costs[i][1]
            dp[i][2]=min(dp[i-1][0],dp[i-1][1])+costs[i][2]
        return min(dp[-1])
