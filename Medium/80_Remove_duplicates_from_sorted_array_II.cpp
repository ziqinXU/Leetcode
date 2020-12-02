class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        for(int i=0; i < nums.size(); i++)
        {
            int count = 0;
            int cur = nums[i];
            int j=i;
            while(j<nums.size() && nums[j] == cur)
            {
                count++;
                j++;
                if(count>=2)
                break;
            }
            while(j<nums.size() && nums[j] == cur)
            {
                nums.erase(nums.begin()+j);
                
            }
            i=j-1;
           

        }
        return nums.size();
    }
};
