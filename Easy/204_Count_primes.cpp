class Solution {
public:
    int countPrimes(int n) {
        vector<int> primearr(n,1);
        int res = 0;
        for(int i=2;i<n;i++)
        {
            if(primearr[i]==1)
            {
                res++;
                if((long long)i*i<n)
                {
                    for(int j=i*i;j<n;j+=i)
                    {
                        primearr[j]=0;
                    }
                }
            }
        }
        return res;
    }


};
