class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) { //循环AB，记录和到hashmap，再从CD和中寻找-AB和。
        int res=0;
        map<int,int>hashAB;
        for(auto a:A)
        {
            for(auto b:B)
            {
                hashAB[a+b]++;
            }
        }
        
        for(auto c:C)
        {
            for(auto d:D)
            {
                if(hashAB.count(-c-d)>0)//存在key
                {
                    res+=hashAB[-c-d];
                }
            }
        }
        return res;
    }
};
