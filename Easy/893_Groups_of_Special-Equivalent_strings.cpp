class Solution {
public:
    int numSpecialEquivGroups(vector<string>& A) {
        map<string,int>hashmap;
        string tempodd;
        string tempeven;
        string temp;
        for(int i=0;i<A.size();i++)
        {
            for(int j=0;j<A[i].size();j=j+2)
            {
                tempodd.push_back(A[i][j]);
            }
            for(int j=1;j<A[i].size();j=j+2)
            {
                tempeven.push_back(A[i][j]);
            }
            sort(tempodd.begin(),tempodd.end());
            sort(tempeven.begin(),tempeven.end());
            temp.append(tempodd);
            temp.append(tempeven);
            hashmap[temp]++;
            temp.clear();
            tempodd.clear();
            tempeven.clear();
        }
        return hashmap.size();
    }
};
