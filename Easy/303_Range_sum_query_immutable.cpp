///first attempt 34.8%faster, 100%less memory
//Idea:Use prefix to save temp sum.
class NumArray {
private:
    vector<int> pre;
public:
    
    NumArray(vector<int>& nums) {
        pre.resize(nums.size()+1,0);
        pre.push_back(0);
        for(int i=0;i<nums.size();i++)//save prefix
        {
            pre[i+1]=pre[i]+nums[i];
        }
        
    }
    
    int sumRange(int i, int j) {//substract
        return pre[j+1]-pre[i];
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(i,j);
 */
