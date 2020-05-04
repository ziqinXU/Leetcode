///first attempt 19.58%faster, 20%less memory
//Idea:
class Solution {
public:
    int distributeCandies(vector<int>& candies) {
    map<int,int>hashmap;
    for(int i=0;i<candies.size();i++)
    {
        hashmap[candies[i]]++;//count the number of candies in each category
    }
   /*if the category number is bigger or equal to the half of whole candies, 
   the sister can get maximum half of it. Otherwise, all sorts of candies.
   */
    if(candies.size()/2<=hashmap.size()) 
    return candies.size()/2;
    else
    return hashmap.size();
    }
};
