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
