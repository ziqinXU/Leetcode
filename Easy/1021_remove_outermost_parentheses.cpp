class Solution {
public:
    string removeOuterParentheses(string S) {
    string returnarray;
    int left=0,start=0;
    int right=0;
    for(int i=0;i<S.size();i++)
    {
        if(S[i]=='(')
        {
            left++;
        }
        if(S[i]==')')
        {
            right++;
        }
        if(left==right)
        {
            returnarray.append(S.substr(start+1,i-start-1));
            start=i+1;
        }
    }
    return returnarray;
    }
};
