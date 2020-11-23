class Solution {
public:
    int countSubstrings(string s, string t) {
        int res=0;
        for(int i=0;i<s.size();i++)
        {
            for(int j=0;j<t.size();j++)
            {
                int k=i,m=j;
                int diff=0;
                while(k<s.size() && m<t.size())
                {
                    if(s[k]!=t[m])
                    {
                        diff++;
                    }
                    if(diff>=2)
                    {
                        break;
                    }
                    if(diff==1)
                    {
                        res++;
                    }
                    k++;
                    m++;
                }
            }
        }
        return res;

    }
};
