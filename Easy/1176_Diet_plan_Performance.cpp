class Solution {
public:
    int dietPlanPerformance(vector<int>& calories, int k, int lower, int upper) {
        vector<int>result;
        int returnnumber=0;
        int count=0;
        int temp=0;
        while(count!=k)
        {
                temp=temp+calories[0+count];
                count++;
        }
         if(temp<lower)
            result.push_back(-1);
            else if(temp>upper)
            result.push_back(1);
            else
            result.push_back(0);
        for(int i=1;i<calories.size()-k+1;i++)
        {
            
            temp=temp-calories[i-1]+calories[i+k-1];
            if(temp<lower)
            result.push_back(-1);
            else if(temp>upper)
            result.push_back(1);
            else
            result.push_back(0);
        }
        for(int i=0;i<result.size();i++)
        {
            returnnumber=returnnumber+result[i];
        }
        return returnnumber;
    }
};
