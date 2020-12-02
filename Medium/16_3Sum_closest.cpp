class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        //先排序，再用指针，固定一个数字位置，左右指针遍历其他数组位置。
        sort(nums.begin(),nums.end());
        int left;
        int right;
        int res=1e5;
        for(int i=0;i<nums.size()-2;i++)
        {
            left = i+1;
            right = nums.size()-1; 
            while(left<right)
            {
                if(nums[i]+nums[left]+nums[right] == target)
                {
                    return target;
                }
                else if (nums[i]+nums[left]+nums[right] < target)
                {
                    if(abs(nums[i]+nums[left]+nums[right] - target)< abs(res-target))
                    {
                        res=nums[i]+nums[left]+nums[right];
                    }
                    left++;
                }
                else
                {
                    if(abs(nums[i]+nums[left]+nums[right] - target)< abs(res-target))
                    {
                        res=nums[i]+nums[left]+nums[right];
                    }
                    right--;
                }
            
            }
        }
        return res;
    }
};
