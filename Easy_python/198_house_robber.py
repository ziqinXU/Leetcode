class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        if len(nums)==0:
            return 0
        dp[0] = nums[0]
        if len(nums)==1:
            return dp[0]
        dp[1] = max(nums[1],nums[0])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        return dp[len(nums)-1]
