///first attempt 50.34%faster, 100%less memory
//Idea:count the left and right parentheses number, if they are the same, add the parentheses inside into the result
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
        if(left==right)//number of left and right are the same
        {
            returnarray.append(S.substr(start+1,i-start-1));//add the parentheses inside into the result
            start=i+1;//start from the new position
        }
    }
    return returnarray;
    }
};
