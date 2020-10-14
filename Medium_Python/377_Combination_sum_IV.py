class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if target==0:
            return 1
        #注意是排序问题，不同顺序有影响
        dp=[0]*(target+1)
        dp[0]=1
        for i in range(1,target+1):
            for j in range(len(nums)):
                if i-nums[j]>=0:
                    dp[i]+=dp[i-nums[j]]
        return dp[-1]
