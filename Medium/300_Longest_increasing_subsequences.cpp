class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> dp(nums.size(), 0);
        if(nums.size()==0)
        {
            return 0;
        }
        for(int i=0;i<nums.size();i++)
        {
            dp[i]=0;
        }
        for(int i=0;i<nums.size();i++)
        {
            int cur=nums[i];
            dp[i]=1;
            for(int j=i-1;j>=0;j--)
            {
                if(nums[j]<cur)
                {
                    dp[i]=max(dp[i],dp[j]+1);
                }
            }
        }

        return *max_element(dp.begin(), dp.end());
    }
};
