class Solution {
public:
    int subarraysDivByK(vector<int>& A, int K) {
        vector<int> P(A.size(),0);
        P[0] = A[0];
        map<int,int> hashmap;
        hashmap[0]=1;
        if(hashmap.find((P[0]%K+K)%K)!=hashmap.end())
        {
            hashmap[(P[0]%K+K)%K]++;
        }
        else
        {
            hashmap[(P[0]%K+K)%K]=1;
        }
        
        for(int i = 1; i < A.size();i++)
        {
            P[i] = P[i-1] + A[i];
            if(hashmap.find((P[i]%K+K)%K)!=hashmap.end())
            {
                hashmap[(P[i]%K+K)%K]++;
            }
            else
            {
                hashmap[(P[i]%K+K)%K]=1;
            }
        }
        int res = 0;
        for(map<int,int>::iterator it = hashmap.begin(); it!=hashmap.end();it++)
        {
            res+=(it->second)*(it->second-1)/2;
        }
        return res;
    }
};
