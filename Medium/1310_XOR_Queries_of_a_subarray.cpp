///first attempt 45.56%faster, 5.06%less memory
//Idea:use vector to save prefix. use XOR of prefixs to calculate prefix from left to right.
class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
    vector<int> returnarray;
    vector<int>prefix;
    prefix.push_back(0);//prefix array starts from 0
    for(int i=1;i<=arr.size();i++)
    {
        prefix.push_back(arr[i-1]^prefix[i-1]);
    }
    for(int i=0;i<queries.size();i++)
    {
        
        returnarray.push_back(prefix[queries[i][0]]^prefix[queries[i][1]+1]);//from left to right inclusive right
    }
    return returnarray;
    }
};
