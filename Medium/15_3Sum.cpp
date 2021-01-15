class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        //数组长度小于3，直接返回
        //排序数组
        //若当前数字大于0，直接返回，若当前等于下一个数组，跳过 // left = i+1 right = n-1
        //如果等于0，移动左右指针，并确保跳过相同的
        //大于，则移动右指针，否则移动左边指针。
        vector<vector<int>> res;
        vector<int> temp;
        if(nums.size() < 3)
        {
            return res;
        }
        else
        {
            sort(nums.begin(),nums.end());
            int left, right;
            for(int i = 0; i < nums.size() - 2 ;i++)
            {
                if(nums[i] > 0)
                {
                    break;
                }
                left = i + 1;
                right = nums.size() - 1;
                while(left < right)
                {
                    if(nums[i] + nums[left] + nums[right] == 0)
                    {
                        temp.push_back(nums[i]);
                        temp.push_back(nums[left]);
                        temp.push_back(nums[right]);
                        res.push_back(temp);
                        temp.clear();    
                        
                        int cur = left;
                        while(cur+1 < nums.size()-1 && nums[left]==nums[cur+1])
                        {
                            cur++;
                        }
                        left = cur +1;
                    }
                    else if(nums[i] + nums[left] + nums[right] < 0)
                    {
                        left++;
                    }
                    else
                    {
                        right--;
                    }
                }    
                int current = i;
                while(current+1 < nums.size()-1 && nums[i]==nums[current+1])
                {
                    current++;
                }
                i = current;
            }     
        }
        return res;
    }
};
