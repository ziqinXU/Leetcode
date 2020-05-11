///first attempt 61.88%faster, 8.82%less memory
//Idea:Sort the array and return the kth largest
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        sort(nums.begin(),nums.end());
        return nums[nums.size()-k];
    }
};
