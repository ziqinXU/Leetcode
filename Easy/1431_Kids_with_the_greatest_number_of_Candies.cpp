class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
    vector<pair<int,int>>sortedcandies;
    pair<int,int>temp[100];
    for(int i=0;i<candies.size();i++)
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
    
    while(current>=0&&sortedcandies[sortedcandies.size()-1].first-sortedcandies[current].first<=extraCandies)
    {
       
        returnarray[sortedcandies[current].second]=true;
        current--;
        
    }
    
    return returnarray;

    }
};
