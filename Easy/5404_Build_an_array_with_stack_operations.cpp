class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
    vector<string> returnarray;
    int i=0,p=1;
    while(1)
    {
        if(target[i]-p!=0)
        {
            returnarray.push_back("Push");
            returnarray.push_back("Pop");
            p++;
        }
        else
        {
            returnarray.push_back("Push");
            i++;
            p++;
        }
        if(i==target.size())
        break;
    }
    return returnarray;
    }
};
