class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        vector<int> dp(nums.size(),0);
        sort(nums.begin(),nums.end());//  排序
        vector<int> res;
        dp[0] = 1;
        for(int i = 1; i < nums.size(); i++)
        {
            int tempmax = 1;
            for(int j = i-1; j >= 0 ;j--)
            {
                if(nums[i] % nums[j] == 0)
                {
                    if(dp[j]+1 > tempmax)
                    {
                        tempmax = dp[j]+1;
                    }
                }
            } 
            dp[i] = tempmax;
            if(dp[i] == 0)
            {
                dp[i] = 1;
            }   
        }//找出最大整除子集大小
        for(int i = 0; i< nums.size();i++)
        {
            cout << dp[i] << endl;
        }
        int maxsize = *max_element(dp.begin(),dp.end());
        int maxvalue;
        for(int i = nums.size()-1; i>=0;i--)
        {
            if(maxsize == dp[i])
            {
                maxvalue = nums[i];
                break;
            }
        }//倒序找出maxsize和alue
        res.push_back(maxvalue);
        int size = maxsize-1;
        while(size > 0)
        {
            for(int i = nums.size()-1;i >= 0; i--)
            {
                if(dp[i] == size && maxvalue % nums[i] == 0)
                {
                    res.push_back(nums[i]);
                    maxvalue = nums[i];//找到能整除当前最大整数的数字并加入结果
                    break;
                }
            }
            
            size--;
        }
        return res;
    }
};
