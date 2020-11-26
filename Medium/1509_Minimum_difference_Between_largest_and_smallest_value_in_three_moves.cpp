class Solution {
public:
    int minDifference(vector<int>& nums) {
        if(nums.size()<=4)
        {
            return 0;
        }
        else
        {
            //改变3大，1小-2大；2小-1大；3小
            sort(nums.begin(),nums.end());
            int length=nums.size()-1;
            int res=INT_MAX;
            if(nums[length-3]-nums[0]<res)
            res=nums[length-3]-nums[0];
            if(nums[length-2]-nums[1]<res)
            res=nums[length-2]-nums[1];
            if(nums[length-1]-nums[2]<res)
            res=nums[length-1]-nums[2];
            if(nums[length]-nums[3]<res)
            res=nums[length]-nums[3];
            return res;
        }
    }
};
