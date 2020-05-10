///first attempt 91.99%faster, 100%less memory
//Idea:start from left, find the same alphabet in the string, mark its end position, when the start position is greater than the end, found the part.
class Solution {
public:
    vector<int> partitionLabels(string S) {
    int start=0;
    int last=0;
    int end=0;
    vector<int> returnarray;
    for(int i=0;i<S.size();i++)
    {
        if(S[start]!='0')//if the alphabet has not been visited
        {
            int k=start;
            int k1=0;
            while(1)//find all alphabets in the string
            {
                k1=S.find(S[start],k+1);
                if(k1==-1)
                break;
                k=k1;
                S[k1]='0';
                if(k1>end)//if the end position has been moved towards right, mark it.
                end=k1;
            }
            S[start]='0';
            
        }
        start++;
        if(start>end)//found the required part,mark its length
        {
            returnarray.push_back(start-last);
            last=start;
        }
        
        
    }
    return returnarray;
    }
};
