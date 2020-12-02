class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        //和三数和类似，固定前两个数，指针后两个数字,可通过不取相邻重复数字达到去重效果
        vector<vector<int>> res;
         if(nums.size()<4)
        {
            return res;
        }
        vector<int> temp;
        int left,right;
        sort(nums.begin(),nums.end());
        for(int i=0;i<nums.size()-3;i++)
        {
            for(int j=i+1;j<nums.size()-2;j++)
            {
                left=j+1;
                right=nums.size()-1;
                while(left<right)
                {
                    if(nums[i]+nums[j]+nums[left]+nums[right]==target)
                    {
                        

                        temp.push_back(nums[i]);
                        temp.push_back(nums[j]);
                        temp.push_back(nums[left]);
                        temp.push_back(nums[right]);
                        
                        if (find(res.begin(),res.end(),temp)==res.end())
                        {
                            res.push_back(temp);
                        }
	                    
                        temp.clear();
                        left++;
                    }
                    else if (nums[i]+nums[j]+nums[left]+nums[right] < target)
                    {
                        left++;
                    }
                    else
                    {
                        right--;
                    }
                }
                
            
            }
            
        }
        return res;

    }
};
