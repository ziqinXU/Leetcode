class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        vector<int>count;
        
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i]==0)
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
            if(nums[i]==1)
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
        /*
                for(int i=0;i<count.size();i++)
        {
            printf("%d ",count[i]);
        } */
        vector<int>intarray;
        int begin=0;
        if(nums[0]==0)
        {
            begin=1;
        }
        if(begin==1&&count.size()==1)
        return 1;
        for(int i=begin;i<count.size();i=i+2)
        {
            if(i+1<count.size()&&count[i+1]==1)
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
            if(i+1<count.size()&&count[i+1]>1)
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
        return intarray[intarray.size()-1];
    }
};
