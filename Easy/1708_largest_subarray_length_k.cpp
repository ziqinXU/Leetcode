class Solution {
public:
    vector<int> largestSubarray(vector<int>& nums, int k) {
        //找到nums.size()-k+1中最大的值，返回长度为k
        auto it = max_element(nums.begin(), nums.end() - k + 1);
        return {it,it+k};
    }
};
