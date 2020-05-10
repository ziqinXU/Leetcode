class Solution {
public:
    vector<int> partitionLabels(string S) {
    int start=0;
    int last=0;
    int end=0;
    vector<int> returnarray;
    for(int i=0;i<S.size();i++)
    {
        if(S[start]!='0')
        {
            int k=start;
            int k1=0;
            while(1)
            {
                k1=S.find(S[start],k+1);
                if(k1==-1)
                break;
                k=k1;
                S[k1]='0';
                if(k1>end)
                end=k1;
            }
            S[start]='0';
            
        }
        start++;
        if(start>end)
        {
            returnarray.push_back(start-last);
            last=start;
        }
        
        
    }
    return returnarray;
    }
};
