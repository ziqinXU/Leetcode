///first attempt 100%faster, 100%less memory
//Idea:Use vector to record position of each 1, and check distance between each 1.
class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {
    vector<int>pos;
    for(int i=0;i<nums.size();i++)//record position of ones.
    {
        if(nums[i]==1)
        pos.push_back(i);
    }
    if(pos.size()>=1)
    {
        
        for(int i=0;i<pos.size()-1;i++)//check the distances
        {
            
            if(pos[i+1]-pos[i]<=k)
            return false;
        }
        
    }
    return true;
    }
};
