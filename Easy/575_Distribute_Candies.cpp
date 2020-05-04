class Solution {
public:
    int distributeCandies(vector<int>& candies) {
    map<int,int>hashmap;
    for(int i=0;i<candies.size();i++)
    {
        hashmap[candies[i]]++;
    }
    if(candies.size()/2<=hashmap.size())
    return candies.size()/2;
    else
    return hashmap.size();
    }
};
