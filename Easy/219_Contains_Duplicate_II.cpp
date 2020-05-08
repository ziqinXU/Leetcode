class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        map<int,int>hashmap;
        int count=0;
        for(int i=0;i<nums.size();i++)
        {
            if(hashmap.count(nums[i])>=1)
            {
                if(i-hashmap[nums[i]]<=k)
                count=1;
                else
                {
                    hashmap[nums[i]]=i;
                }
            }
            else
            {
                hashmap[nums[i]]=i;
            }
        }
        if(count==0)
        return false;
        else
        return true;
    }
};
