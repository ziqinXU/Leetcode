class Solution {
public:
    int maxSubArray(vector<int>& nums) {
    int max=INT_MIN;
    int currentsum;
    int previoussum=0;
    for(int i=0;i<nums.size();i++)
    {
        if(previoussum<0)
        previoussum=0;
        currentsum=previoussum+nums[i];
        previoussum=currentsum;
        if(currentsum>max)
        max=currentsum;
    }
    return max;
    }
};
