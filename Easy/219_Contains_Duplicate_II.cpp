///first attempt 6.64%faster, 5.55%less memory
//Idea:use hashmap to save the position , if found one that for the same number, the distance is less or equal to k, true, not found, false
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        map<int,int>hashmap;
        int count=0;
        for(int i=0;i<nums.size();i++)
        {
            if(hashmap.count(nums[i])>=1)//the number already visited
            {
                if(i-hashmap[nums[i]]<=k)//found the number meets the requirement
                count=1;
                else
                {
                    hashmap[nums[i]]=i;
                }
            }
            else
            {
                hashmap[nums[i]]=i;//the number never visited 
            }
        }
        if(count==0)
        return false;
        else
        return true;
    }
};
