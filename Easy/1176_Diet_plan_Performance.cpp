///first attempt 9.2%faster, 50%less memory
//Idea: count the sum within k days and save them in an array with criteria, lower than lower -1, higher than upper +1
//pay attention to the time limit problem here!!!
//instead of counting the sum each time when moving the sliding window, remove the element from last sum and add the new element
class Solution {
public:
    int dietPlanPerformance(vector<int>& calories, int k, int lower, int upper) {
        vector<int>result;
        int returnnumber=0;
        int count=0;
        int temp=0;
        while(count!=k)//sum for first k days
        {
                temp=temp+calories[0+count];
                count++;
        }
         if(temp<lower)//check the criteria
            result.push_back(-1);
            else if(temp>upper)
            result.push_back(1);
            else
            result.push_back(0);
        for(int i=1;i<calories.size()-k+1;i++)//moving the sliding window, add one element and remove the one from last,check it again iteratively
        {
            
            temp=temp-calories[i-1]+calories[i+k-1];
            if(temp<lower)
            result.push_back(-1);
            else if(temp>upper)
            result.push_back(1);
            else
            result.push_back(0);
        }
        for(int i=0;i<result.size();i++) //count the sum of the result array and return it
        {
            returnnumber=returnnumber+result[i];
        }
        return returnnumber;
    }
};
