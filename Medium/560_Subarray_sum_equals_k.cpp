class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int pre = 0;
        int res = 0;
        map<int,int>hashmap;
        hashmap[0]=1;//add 0 for single number = 0
        for(int i = 0; i< nums.size();i++)
        {
            pre += nums[i];
            if(hashmap.find(pre-k) != hashmap.end())
            {
                res += hashmap[pre-k];
            }
            if(hashmap.find(pre) != hashmap.end())
            {
                hashmap[pre]++;
            }
            else
            {
                hashmap[pre] = 1;
            }
        }
        
        return res;
    }
};
