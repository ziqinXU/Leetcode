///first attempt 100%faster, 100%less memory
//Idea:Sort the array with number of candies for each kid, compare the maximum candy and the current candy, if 
//being added the extra candy number, the sum exeeds or equal to the maximum number, return true, otherwise, false.
class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
    vector<pair<int,int>>sortedcandies;
    pair<int,int>temp[100];
    for(int i=0;i<candies.size();i++)//sort the array with candy number
    {
        temp[i].first=candies[i];
        temp[i].second=i;
        sortedcandies.push_back(temp[i]);
    }
    vector<bool> returnarray;
    for(int i=0;i<candies.size();i++)
    {
        returnarray.push_back(false);
    }
    sort(sortedcandies.begin(),sortedcandies.end());
    int current=sortedcandies.size()-1;
    //check whether with extra candies, the kid can have the same or more candies than the maximum, if so, return true;
    while(current>=0&&sortedcandies[sortedcandies.size()-1].first-sortedcandies[current].first<=extraCandies)
    { 
        returnarray[sortedcandies[current].second]=true;
        current--;
    }
    
    return returnarray;
    }
};
