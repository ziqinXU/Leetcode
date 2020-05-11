///first attempt 100%faster, 100%less memory
//Idea:If the number is not in the array, add push and pop, if it is in, add push
class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
    vector<string> returnarray;
    int i=0,p=1;
    while(1)
    {
        if(target[i]-p!=0)//not in the array, push first and then pop
        {
            returnarray.push_back("Push");
            returnarray.push_back("Pop");
            p++;
        }
        else
        {
            returnarray.push_back("Push");//in the array, push
            i++;
            p++;
        }
        if(i==target.size())
        break;
    }
    return returnarray;
    }
};
