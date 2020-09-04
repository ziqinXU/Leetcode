# 如果当前可根据[0:i]范围内到达i，且此范围内的j点本身也可被到达，即成功
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp=[0]*len(nums)
        dp[0]=1
        for i in range(1,len(nums)):
            for j in reversed(range(0,i)):
                if nums[j]>=i-j and dp[j]==1:
                    dp[i]=1
                    break
        if dp[-1]==1:
            return True
        else:
            return False
