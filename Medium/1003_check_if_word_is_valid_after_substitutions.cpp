///first attempt 48.52%faster, 100%less memory
//Idea:If there is no string "abc" in the array, return false
//use a vector to save temp array. if found c, check the previoud two, if b and a exist, pop all, otherwise return false
//if the vector is empty at the end, return true, otherwise false
class Solution {
public:
    bool isValid(string S) {
        vector<int>stringarray;
        if(S.find("abc")==-1)
        return false;
        int p=0;
        for(int i=0;i<S.size();i++)
        {
            stringarray.push_back(S[i]);
            
            if(stringarray[p]=='c')
            {
                if(p-1>0&&stringarray[p-1]=='b'&&p-2>=0&&stringarray[p-2]=='a')
                {
                    stringarray.pop_back();
                    stringarray.pop_back();
                    stringarray.pop_back();
                    p=p-3;
                }
                else
                return false;
            }
            p++;
        }
        if(stringarray.empty()==1)
        return true;
        else
        return false;
    }
};
