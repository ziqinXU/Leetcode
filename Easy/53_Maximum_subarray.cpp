///first attempt 97.44%faster, 100%less memory
//Idea:Use variable:currentsum,previoussum,max. If previoussum is less than 0, let it be 0. 
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
    int max=INT_MIN;
    int currentsum;
    int previoussum=0;
    for(int i=0;i<nums.size();i++)
    {
        if(previoussum<0)//if the previous sum is less than 0, let it be zero
        previoussum=0;
        currentsum=previoussum+nums[i];
        previoussum=currentsum;
        if(currentsum>max)//check the maximum value
        max=currentsum;
    }
    return max;
    }
};
