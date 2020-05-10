class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
    vector<int> returnarray;
    vector<int>prefix;
    prefix.push_back(0);
    for(int i=1;i<=arr.size();i++)
    {
        prefix.push_back(arr[i-1]^prefix[i-1]);
    }
    for(int i=0;i<queries.size();i++)
    {
        
        returnarray.push_back(prefix[queries[i][0]]^prefix[queries[i][1]+1]);
    }
    return returnarray;
    }
};
