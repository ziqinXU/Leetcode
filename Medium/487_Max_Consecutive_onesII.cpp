///first attempt 30.1%faster, 25%less memory
//Idea:save how many 1s and 0s are there successively.
//If there is only one 0 between 2 1s, add all 1+ one 0, otherwise only one 1 + one 0.
//find the longest 1s
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        vector<int>count;
        
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i]==0)//count 0s successively
            {
                int j=i+1;
                while(j<nums.size()&&nums[j]==0)
                {
                    j++;
                }
                count.push_back(j-i);
                i=j-1;
                continue;
            }
            if(nums[i]==1)//count 1s successively
            {
                int j=i+1;
                while(j<nums.size()&&nums[j]==1)
                {
                    j++;
                }
                count.push_back(j-i);
                i=j-1;
                continue;
            }
        }
        vector<int>intarray;
        int begin=0;
        if(nums[0]==0)
        {
            begin=1;
        }
        if(begin==1&&count.size()==1)//if only 0s, return 1
        return 1;
        for(int i=begin;i<count.size();i=i+2)
        {
            if(i+1<count.size()&&count[i+1]==1)//if only 1 zero, add all
            {
                if(i+2<count.size())
                {
                    intarray.push_back(count[i]+1+count[i+2]);
                }
                else
                {
                    intarray.push_back(count[i]+1);
                }
            }
            if(i+1<count.size()&&count[i+1]>1)//more than one 0, +1
            {
                intarray.push_back(count[i]+1);
            }
            if(i+1==count.size())
            {
                intarray.push_back(count[i]);
            }

        }
        sort(intarray.begin(),intarray.end());
        if(begin==1&&count.size()==2)
        return intarray[intarray.size()-1]+1;
        return intarray[intarray.size()-1];//find the max ones
    }
};
