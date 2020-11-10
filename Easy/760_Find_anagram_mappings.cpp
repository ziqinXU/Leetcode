class Solution {
public:
    vector<int> anagramMappings(vector<int>& A, vector<int>& B) {
        map<int,int> hashmapB;
        for(int i=0;i < B.size();i++)
        {
            hashmapB[B[i]] = i;
        }
        vector<int> res;
        for(int i=0;i < A.size();i++)
        {
            res.push_back(hashmapB[A[i]]);
        }
        return res;
    }
};
