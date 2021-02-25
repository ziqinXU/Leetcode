class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        int maxlength = 0;
        multiset<int> s;
        int left = 0;
        int right = 0;
        while(right < nums.size())
        {
            s.insert(nums[right]);
            while(*s.rbegin()-*s.begin() > limit)//反向迭代器
            {
                s.erase(s.find(nums[left]));
                left++;
            }
            if(right-left+1>maxlength)
                maxlength = right-left+1;
            right++;
           
        }
        
        return maxlength;
    }
};
