class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #动态规划，找到比当前元素小的数字的sublen+1，求当前可达到最大长度
        if len(nums)==0:
            return 0
        f=[1]*len(nums)
        for j in range(len(nums)):
            for i in range(j):
                if nums[j]>nums[i]:
                    f[j]=max(f[i]+1,f[j])
        return max(f)
