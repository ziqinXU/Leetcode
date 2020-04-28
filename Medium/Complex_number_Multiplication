class Solution {
public:
    string complexNumberMultiply(string a, string b) {
       int a1,a2,b1,b2;
       int pos1,pos2;
       string returnarray;
       for(int i=0;i<a.size();i++)
        {
            if(a[i]=='+')
            pos1=i;
            if(a[i]=='i')
            pos2=i;
        }
        a1=stoi(a.substr(0,pos1));
        a2=stoi(a.substr(pos1+1,pos2));
       // printf("%d %d",a1,a2);
       for(int i=0;i<b.size();i++)
        {
            if(b[i]=='+')
            pos1=i;
            if(b[i]=='i')
            pos2=i;
        }
        b1=stoi(b.substr(0,pos1));
        b2=stoi(b.substr(pos1+1,pos2));
        returnarray.append(to_string(a1*b1-a2*b2));
        returnarray.push_back('+');
        returnarray.append(to_string(a1*b2+a2*b1));
        returnarray.push_back('i');
        return returnarray;
    }
};
