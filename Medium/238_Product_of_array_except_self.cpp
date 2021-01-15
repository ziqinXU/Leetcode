class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res(nums.size(),1);
        int R = 1;
        for(int i = 1;i < nums.size();i++)
        {
            res[i] = nums[i-1] * res[i-1];
        }//前缀
        for(int i = nums.size()-2; i>= 0 ; i--)
        {
            res[i] = res[i] * (nums[i+1]*R);
            R = nums[i+1]*R;
        }//后缀
        return res;
    }
};
