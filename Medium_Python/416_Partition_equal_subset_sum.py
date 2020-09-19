#01背包问题
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        arrsum=sum(nums)
        if arrsum%2!=0:
            return False
        halfsum=arrsum//2
        dp=[[0]*(halfsum+1) for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(halfsum+1):
                if i==0:
                    if nums[0]<=j:
                        dp[0][j]=nums[0]
                else:
                    if j-nums[i]>=0:
                        dp[i][j]=max(dp[i-1][j-nums[i]]+nums[i],dp[i-1][j])
                        if dp[i][j]==halfsum:
                            #print(dp)
                            return True
                    else:
                        dp[i][j]=dp[i-1][j]
        #print(dp)
        return False
        
