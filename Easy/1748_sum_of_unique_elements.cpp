class Solution {
public:
    int sumOfUnique(vector<int>& nums) {
        map<int,int>hashmap;
        int res = 0;
        for(int i = 0; i < nums.size(); i++)
        {
            if(hashmap.find(nums[i])==hashmap.end())
            {
                hashmap[nums[i]] = 1;
            }
            else
            {
                hashmap[nums[i]]++;
            }
        }
        for (auto& [key, value]: hashmap) 
        {
            if(value==1)
            {
                res += key;
            }
        }
        return res;
    }
};
