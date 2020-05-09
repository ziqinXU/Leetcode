class Solution {
public:
    int missingElement(vector<int>& nums, int k) {
        int rest=INT_MAX;
        for(int i=0;i<nums.size()-1;i++)
        {
            
            if(nums[i+1]-nums[i]>1)
            {
                rest=k-(nums[i+1]-nums[i]-1);
                
            }
            
            if(rest<=0)
            return nums[i]+k;
            k=k-(nums[i+1]-nums[i]-1);
        }
        
        if(k>0)
        return nums[nums.size()-1]+k;
        return 0;
    }
};
