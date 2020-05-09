///first attempt 38.89%faster, 100%less memory
//Idea: if there is a gap between two number,substrct the missing number from k and until no k left. If there is still missing number
//at the end, add the corresponding number.
class Solution {
public:
    int missingElement(vector<int>& nums, int k) {
        int rest=INT_MAX;
        for(int i=0;i<nums.size()-1;i++)
        {
            
            if(nums[i+1]-nums[i]>1)//if there is a gap
            {
                rest=k-(nums[i+1]-nums[i]-1);//check remaining number
                
            }
            
            if(rest<=0)//already within the gap
            return nums[i]+k;
            k=k-(nums[i+1]-nums[i]-1);//otherwise check remining number
        }
        
        if(k>0)
        return nums[nums.size()-1]+k;//exceed the array
        return 0;
    }
};
